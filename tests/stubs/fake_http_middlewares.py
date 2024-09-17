from dataclasses import dataclass
from python_middlewareable import (
    MiddlewareBase,
    MiddlewareNextCallBase,
    MiddlewareableBase,
    RequestBase,
)


@dataclass
class HttpRequest(RequestBase):
    headers: dict[str, str]
    method: str


class HttpMiddlewareable(MiddlewareableBase[HttpRequest]):
    pass


class HttpMiddleware(MiddlewareBase[HttpRequest]):
    pass


class AddHeaderMiddleware(HttpMiddleware):
    async def handle(
        self,
        request: HttpRequest,
        next_call: MiddlewareNextCallBase[HttpRequest],
    ):
        request.headers["X-Test"] = "True"
        await next_call(request)


class ModifyMethodMiddleware(HttpMiddleware):
    async def handle(
        self,
        request: HttpRequest,
        next_call: MiddlewareNextCallBase[HttpRequest],
    ):
        request.method = "POST"
        await next_call(request)
