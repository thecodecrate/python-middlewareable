from dataclasses import dataclass
from python_middlewareable import (
    MiddlewareBase,
    MiddlewareNextCallBase,
    RequestBase,
    RequestDataBase,
    ResponseDataBase,
    TransportDataBase,
    DataStructurableRequestMixin,
)


@dataclass
class RequestData(RequestDataBase):  # inherit from RequestDataBase
    name: str


@dataclass
class ResponseData(ResponseDataBase):  # inherit from ResponseDataBase
    value: str = ""


@dataclass
class Request(
    DataStructurableRequestMixin[RequestData, ResponseData, TransportDataBase],
    RequestBase,
):
    pass


class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> Request:
        request.response_data.value += (
            request.request_data.name + " from OneMiddleware"
        )

        return await next_call(request)
