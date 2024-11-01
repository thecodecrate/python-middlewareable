from abc import abstractmethod
from typing import Any
from thecodecrate_pipeline import Processor, T_in, T_out

from .middleware_callable import MiddlewareCallable
from .middleware_processor_interface import (
    MiddlewareProcessorInterface,
)


class MiddlewareProcessor(
    Processor[T_in, T_out],
    MiddlewareProcessorInterface,
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: tuple[MiddlewareCallable, ...],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
