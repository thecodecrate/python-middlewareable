from dataclasses import dataclass
from src.middleware import Middleware as MiddlewareBase
from src.middleware import MiddlewareNextCall as MiddlewareNextCallBase
from src.request import Request as RequestBase
from src.traits.data_structurable.dtos.request_data import (
    RequestData as RequestDataBase,
)
from src.traits.data_structurable.dtos.response_data import (
    ResponseData as ResponseDataBase,
)
from src.traits.data_structurable.dtos.transport_data import (
    TransportData as TransportDataBase,
)
from src.traits.data_structurable.mixins.request_mixin import (
    RequestMixin as DataStructurableRequestMixin,
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
        request.response_data.value += request.request_data.name + " from OneMiddleware"

        await next_call(request)
