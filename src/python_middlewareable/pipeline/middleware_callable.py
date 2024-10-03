from typing import Awaitable, Callable

from ..classes.middleware_interface import MiddlewareInterface
from ..classes.types import MiddlewareNextCall, TRequest


MiddlewareCallable = (
    MiddlewareInterface[TRequest]
    | Callable[[TRequest, MiddlewareNextCall[TRequest]], Awaitable[TRequest]]
    | Callable[[TRequest, MiddlewareNextCall[TRequest]], TRequest]
)
