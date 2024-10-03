from typing import Awaitable, Callable, TypeVar

TRequest = TypeVar("TRequest")

MiddlewareNextCall = Callable[[TRequest], Awaitable[TRequest]]
