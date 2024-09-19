from abc import ABC
from typing import Awaitable, Callable, Generic, TypeVar
from .request import Request

TRequest = TypeVar("TRequest", bound=Request)

MiddlewareNextCall = Callable[[TRequest], Awaitable[TRequest]]


class Middleware(Generic[TRequest], ABC):
    async def handle(
        self,
        request: TRequest,
        next_call: MiddlewareNextCall[TRequest],
    ) -> TRequest:
        return await next_call(request)
