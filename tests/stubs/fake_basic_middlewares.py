from dataclasses import dataclass
from src.middleware import Middleware as MiddlewareBase
from src.middleware import MiddlewareNextCall as MiddlewareNextCallBase
from src.request import Request as RequestBase


@dataclass
class Request(RequestBase):
    name: str
    response: str = ""


class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> None:
        print("OneMiddleware before")

        request.response = f"Hello, {request.name}"

        request.response += " from OneMiddleware"

        await next_call(request)

        print("OneMiddleware after")


class TwoMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> None:
        print("TwoMiddleware before")

        request.response += " from TwoMiddleware"

        await next_call(request)

        print("TwoMiddleware after")
