# Python-Middlewareable

A simple library for working with middlewares in Python.

## Installation

```bash
pip install python-middlewareable
```

## Usage

### 1. Define a payload structure

```python
@dataclass
class Request(RequestBase): # inherit from RequestBase
    value: str
```

### 2. Create a middleware

```python
class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        # do something before the next middleware
        print("OneMiddleware before")

        # modify the request
        request.value = f"Hello, {request.value} from OneMiddleware"

        # call the next middleware
        result = await next_call(request)

        # do something after the next middleware
        print("OneMiddleware after")

        # return the result
        return result
```

### 3. Add the `MiddlewareableBase` trait to the class that will use the middlewares

```python
class App(MiddlewareableBase[Request]):
    middlewares = [OneMiddleware] # add your middlewares here
```

### 4. Instantiate and use it

```python
# middlewareable
app = App()

# process request
result = await app.process_middlewares(Request(value="Hello"))

# check the result
print(request)

# output:
# OneMiddleware before
# OneMiddleware after
# Hello from OneMiddleware
```

## Traits

You can use the following traits to extend the functionality of this library:

- [AutoStructurable](src/python_middlewareable/traits/auto_structurable)
- [DataStructurable](src/python_middlewareable/traits/data_structurable)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
