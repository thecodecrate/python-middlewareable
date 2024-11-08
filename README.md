# TheCodeCrate's Middlewareable

This package provides a middleware pattern implementation built on top of the [`thecodecrate-pipeline`](https://github.com/thecodecrate/python-pipeline) library.

## Installation

```bash
pip install thecodecrate-middlewareable
```

## Middleware Pattern

The middleware pattern allows you to easily compose sequential stages by chaining stages.

In this implementation, the interfaces consist of two parts:

- `MiddlewareStage`
- `MiddlewarePipeline`

A pipeline consists of zero, one, or multiple stages. A pipeline can process a payload. During the processing, the payload will be passed to the first stage. From that moment on, the resulting value is passed on from stage to stage.

This particular implementation is build on top of the `thecodecrate-pipeline` library, which provides a generic pipeline pattern.

The standard processor in Pipeline executes stages in a for-loop manner:

```python
result = payload

for stage in stages:
    result = stage(result)

return result
```

This library provides a middleware processor for executing stages in a nested manner:

```python
stage3 = lambda payload: payload + 3
stage2 = lambda payload: stage3(payload) + 2
stage1 = lambda payload: stage2(payload) + 1

result = stage1(payload)
```

This is useful for implementing a chain of responsibility, where each stage can perform pre-processing, post-processing, or modify the payload.

## Usage

You define middleware as callables that accept a payload and a `next_call` function:

```python
# Create a middleware pipeline using lambda functions
pipeline = (
    MiddlewarePipeline[int]()
    .pipe(lambda x, next_call: next_call(x + 1))
    .pipe(lambda x, next_call: next_call(x * 2))
    .pipe(lambda x, next_call: next_call(x + 3))
)

# Process a payload
result = await pipeline.process(5)
print(f"Result: {result}")
```

This pipeline processes the payload `5` through the following stages:

1. Add 1: `5 + 1 = 6`
2. Multiply by 2: `6 * 2 = 12`
3. Add 3: `12 + 3 = 15`

**Output:**

```plaintext
Result: 15
```

With middlewares, you can include pre-processing and post-processing logic:

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
pipeline = (
    MiddlewarePipeline()
    .pipe(middleware_one)
    .pipe(middleware_two)
)

# Process a payload
result = await pipeline.process(5)
print(f"Result: {result}")
```

**Output:**

```plaintext
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
    async def __call__(self, payload: int, next_call: MiddlewareNextCall) -> int:
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

Middlewareable is designed as a processor for the `thecodecrate-pipeline` library, allowing seamless integration and enhanced functionality.

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

For proper type-hinting, use the `MiddlewarePipeline` class:

```python
...
# Create a pipeline with the middleware processor
pipeline = MiddlewarePipeline(processor=MiddlewareProcessor()).pipe(middleware_stage)
result = await pipeline.process(5)
```

## Declarative Middleware

You can declare middleware stages directly in your pipeline class:

```python
class MyMiddlewarePipeline(MiddlewarePipeline[int, int]):
    stages = (
        middleware_one,
        middleware_two,
    )

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
