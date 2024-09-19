# `DataStructurable` Trait

This trait implements an opinionated way to structure the request payload.

The request payload has the following structure:

- Request data
  - The original data sent for processing
  - Ex. `{name, age}`
  - This attribute is immutable and should not be changed
- Response data
  - Middlewares modify this attribute to form the final response
  - Ex. `{name: 'John', age: 30}`
- Transport data
  - Middlewares can use this attribute for flow control
  - Ex. `{status_code: 200, headers: {}}`

## Usage

### 1. Define a request structure

```python
@dataclass
class RequestData(RequestDataBase): # inherit from RequestDataBase
    name: str
```

### 2. Define a response structure

```python
@dataclass
class ResponseData(ResponseDataBase):  # inherit from ResponseDataBase
    value: str = ""
```

### 3. Add `DataStructurableRequestMixin` to the request class

```python
@dataclass
class Request(
    DataStructurableRequestMixin[RequestData, ResponseData, TransportDataBase],
    RequestBase,
):
    pass
```

The trait adds the following attributes to `Request`:

- `request_data: RequestData`
  - This attribute is immutable and should not be changed
- `response_data: ResponseData`
  - Middlewares modify this attribute to form the final response
- `transport_data: TransportData`
  - Create a custom class from `TransportDataBase` to store your middlewares' data

### 4. Use the structured format in the middlewares

```python
class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        request.response_data.value = request.request_data.name + " from OneMiddleware"

        return await next_call(request)
```

### 5. Add `DataStructurable` to the middlewareable

```python
class App(DataStructurable, MiddlewareableBase[Request]):
    middlewares = [OneMiddleware]
```

### 6. Instantiate and use it

```python
# middlewareable
app = App()

# request
request = Request(
    request_data=RequestData(name="John"),
    response_data=ResponseData(value=""),
    transport_data=TransportDataBase(),
)

# process request
result = await app.process_middlewares(request)

# check the result
print(result)

# output:
# Request(
#   request_data=RequestData(name='John'),
#   response_data=ResponseData(value='John from OneMiddleware'),
#   transport_data=TransportDataBase()
# )
```
