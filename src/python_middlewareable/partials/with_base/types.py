from typing import Any, Awaitable, Callable


MiddlewareNextCall = Callable[[Any], Awaitable[Any]]
