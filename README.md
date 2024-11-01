# TheCodeCrate's Middlewareable

This package provides a middleware pattern implementation built on top of the [`thecodecrate-pipeline`](https://pypi.org/project/thecodecrate-pipeline/) library.

## Installation

```bash
pip install thecodecrate-middlewareable
```

## Middleware Pattern

The middleware pattern allows you to wrap and compose functions, enabling concerns like logging, authentication, and more to be added transparently.

In this implementation, the core interfaces consist of:

- `MiddlewareStage`
- `MiddlewarePipeline`
- `MiddlewareProcessor`

A `MiddlewarePipeline` processes a payload through a series of middleware functions or stages. Each middleware receives the payload and a `next_call` function, which it can call to pass control to the next middleware in the chain.

## Usage

You can define middleware as callables that accept a payload and a `next_call` function:

```python
# Define middleware functions
async def middleware_one(payload, next_call):
    # Pre-processing
    print("Middleware One - Before")
    payload += 1
    # Call the next middleware
    result = await next_call(payload)
    # Post-processing
    print("Middleware One - After")
    return result

async def middleware_two(payload, next_call):
    print("Middleware Two - Before")
    payload *= 2
    result = await next_call(payload)
    print("Middleware Two - After")
    return result

# Create a middleware pipeline
pipeline = MiddlewarePipeline().pipe(middleware_one).pipe(middleware_two)

# Process a payload
result = await pipeline.process(5)
print(f"Result: {result}")
```

**Output:**

```
Middleware One - Before
Middleware Two - Before
Middleware Two - After
Middleware One - After
Result: 12
```

## Class-Based Middleware

You can also define middleware as classes by implementing the `MiddlewareStage` interface:

```python
class AddMiddleware(MiddlewareStage[int, int]):
    async def __call__(self, payload: int, next_call: MiddlewareNextCall[int, int]) -> int:
        print("AddMiddleware - Before")
        payload += 3
        result = await next_call(payload)
        print("AddMiddleware - After")
        return result

# Use the class-based middleware
pipeline = MiddlewarePipeline().pipe(AddMiddleware())
result = await pipeline.process(5)
print(f"Result: {result}")
```

## Integration with TheCodeCrate Pipeline

`thecodecrate-middlewareable` is designed as a processor for the `thecodecrate-pipeline` library, allowing seamless integration and enhanced functionality.

```python
from thecodecrate_pipeline import Pipeline
from thecodecrate_middlewareable import MiddlewareProcessor

# Define middleware stages
async def middleware_stage(payload, next_call):
    # Middleware logic
    return await next_call(payload)

# Create a pipeline with the middleware processor
pipeline = Pipeline(processor=MiddlewareProcessor()).pipe(middleware_stage)
result = await pipeline.process(5)
```

## Declarative Middleware

You can declare middleware stages directly in your pipeline class:

```python
class MyMiddlewarePipeline(MiddlewarePipeline[int, int]):
    stages = [
        middleware_one,
        middleware_two,
    ]

# Use the declarative pipeline
pipeline = MyMiddlewarePipeline()
result = await pipeline.process(5)
```

## Custom Processors

Custom processors can be created to modify how the middleware pipeline processes stages:

```python
class MyCustomMiddlewareProcessor(MiddlewareProcessor):
    # Override methods as needed
    pass

# Use the custom processor
pipeline = MiddlewarePipeline(processor=MyCustomMiddlewareProcessor())
```

## Exception Handling

Exceptions thrown within middleware are propagated up the call stack. Handle exceptions as needed:

```python
async def error_middleware(payload, next_call):
    if payload < 0:
        raise ValueError("Negative payload not allowed")
    return await next_call(payload)

pipeline = MiddlewarePipeline().pipe(error_middleware)

try:
    result = await pipeline.process(-1)
except ValueError as e:
    print(f"Error: {e}")
```

## License

This project is licensed under the MIT License.
