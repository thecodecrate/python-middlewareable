# `AutoStructurable` Trait

The `AutoStructurable` trait is a helper built on top of the `DataStructurable` trait. It allows you to process middlewares using a payload data directly, without the need to create a request object manually.

The `AutoStructurable` trait adds a `process_middlewares_from_payload` method to the class.

**Example:**

```python
result = await app.process_middlewares_from_payload(data=Payload(name="John"))
```

The `process_middlewares_from_payload` method automatically creates a new request object, based on the payload data, and processes it through the middlewares.

## Usage

### 1. Implement as you would with `DataStructurable`

```python
# define a payload structure
@dataclass
class RequestData(RequestDataBase):  # inherit from RequestDataBase
    name: str


# define a response structure
@dataclass
class ResponseData(ResponseDataBase):  # inherit from ResponseDataBase
    value: str = ""


# add the `DataStructurableRequestMixin` to the request class
@dataclass
class Request(
    DataStructurableRequestMixin[RequestData, ResponseData, TransportDataBase],
    RequestBase,
):
    pass


# create a middleware
class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        request.response_data.value += request.request_data.name + " from OneMiddleware"

        result = await next_call(request)

        return result
```

### 2. Add `AutoStructurable` to the middlewareable

```python
class App(
    AutoStructurable[Request, ResponseData, TransportDataBase],
    MiddlewareableBase[Request],
):
    middlewares = [OneMiddleware]

    # same classes passed to "AutoStructurable" above
    request_class = Request
    response_data_class = ResponseData
    transport_data_class = TransportDataBase
```

**NOTE:** `AutoStructurable` automatically adds the `DataStructurable` trait to the class.

### 3. Instantiate and use it

```python
# middlewareable
app = App()

# process request
result = await app.process_middlewares_from_payload(data=RequestData(name="John"))

# check the result
print(result)

# output:
# ResponseData(value='John from OneMiddleware')
```
