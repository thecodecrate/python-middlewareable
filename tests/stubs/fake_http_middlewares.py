from dataclasses import dataclass
from src.middleware import Middleware, MiddlewareNextCall
from src.middlewareable import Middlewareable
from src.request import Request


@dataclass
class HttpRequest(Request):
    headers: dict[str, str]
    method: str


class HttpMiddlewareable(Middlewareable[HttpRequest]):
    pass


class HttpMiddleware(Middleware[HttpRequest]):
    pass


class AddHeaderMiddleware(HttpMiddleware):
    async def handle(
        self,
        request: HttpRequest,
        next_call: MiddlewareNextCall[HttpRequest],
    ):
        request.headers["X-Test"] = "True"
        await next_call(request)


class ModifyMethodMiddleware(HttpMiddleware):
    async def handle(
        self,
        request: HttpRequest,
        next_call: MiddlewareNextCall[HttpRequest],
    ):
        request.method = "POST"
        await next_call(request)
