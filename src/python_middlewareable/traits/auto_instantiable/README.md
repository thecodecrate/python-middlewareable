# `AutoInstantiable` Trait

The `AutoInstantiable` trait is a helper built on top of the `DataStructurable` trait. It allows you to process middlewares using a payload data directly, without the need to create a request object manually.

The `AutoInstantiable` trait adds a `process_middlewares_from_payload` method to the class.

**Example:**

```python
result = await app.process_middlewares_from_payload(data=Payload(name="John"))
```

The `process_middlewares_from_payload` method automatically creates a new request object, based on the payload data, and processes it through the middlewares.

## Usage

### 1. Implement as you would with `DataStructurable`

```python
# define the payload structure
@dataclass
class PayloadData(RequestDataBase):  # inherit from RequestDataBase
    name: str


# define the response structure
@dataclass
class ResponseData(ResponseDataBase):  # inherit from ResponseDataBase
    value: str = ""


# add the `DataStructurableRequestMixin` to the request class
@dataclass
class Request(
    DataStructurableRequestMixin[PayloadData, ResponseData, TransportDataBase],
    RequestBase,
):
    pass


# create a middleware
class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> None:
        await next_call(request)

        request.response_data.value += request.request_data.name + " from OneMiddleware"
```

### 2. Add `AutoInstantiable` to the middlewareable

```python
class App(
    AutoInstantiable[Request, ResponseData, TransportDataBase],
    MiddlewareableBase[Request],
):
    middlewares = [OneMiddleware]

    # same classes passed to "AutoInstantiable" above
    request_class = Request
    response_data_class = ResponseData
    transport_data_class = TransportDataBase
```

**NOTE:** `AutoInstantiable` automatically adds the `DataStructurable` trait to the class.

### 3. Instantiate and use it

```python
# middlewareable
app = App()

# process request
result = await app.process_middlewares_from_payload(data=PayloadData(name="John"))

# check the result
print(result)

# output:
# ResponseData(value='John from OneMiddleware')
```
