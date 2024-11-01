from typing import Any, Protocol
from thecodecrate_pipeline import ProcessorInterface, T_in, T_out

from .middleware_callable import MiddlewareCallable


class MiddlewareProcessorInterface(
    ProcessorInterface[T_in, T_out],
    Protocol,
):
    async def process(
        self,
        payload: T_in,
        stages: tuple[MiddlewareCallable, ...],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
