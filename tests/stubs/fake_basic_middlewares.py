from dataclasses import dataclass
from python_middlewareable import (
    MiddlewareBase,
    MiddlewareNextCallBase,
    RequestBase,
)


@dataclass
class Request(RequestBase):
    value: str


class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        print("OneMiddleware before")

        request.value = f"Hello, {request.value} from OneMiddleware"

        result = await next_call(request)

        print("OneMiddleware after")

        return result


class TwoMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        print("TwoMiddleware before")

        request.value += " from TwoMiddleware"

        result = await next_call(request)

        print("TwoMiddleware after")

        return result
