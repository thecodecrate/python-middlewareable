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
class PayloadData(RequestDataBase):  # inherit from RequestDataBase
    name: str


@dataclass
class ResponseData(ResponseDataBase):  # inherit from ResponseDataBase
    value: str = ""


@dataclass
class Request(
    DataStructurableRequestMixin[PayloadData, ResponseData, TransportDataBase],
    RequestBase,
):
    pass


class OneMiddleware(MiddlewareBase[Request]):
    async def handle(
        self, request: Request, next_call: MiddlewareNextCallBase[Request]
    ) -> None:
        request.response_data.value += (
            request.request_data.name + " from OneMiddleware"
        )

        await next_call(request)
