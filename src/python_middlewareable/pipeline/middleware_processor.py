from typing import Any, Generic
from thecodecrate_pipeline import (
    ProcessorInterface,
)

from .middleware_callable import MiddlewareCallable
from ..classes.types import TRequest


class MiddlewareProcessor(ProcessorInterface[TRequest], Generic[TRequest]):
    async def process(
        self,
        payload: TRequest,
        stages: list[MiddlewareCallable[TRequest]],
        *args: Any,
        **kwds: Any,
    ) -> TRequest:
        return await self.process_middlewares(
            request=payload, middlewares=stages, *args, **kwds
        )

    async def process_middlewares(
        self,
        request: TRequest,
        middlewares: list[MiddlewareCallable[TRequest]],
        index: int = 0,
        *args: Any,
        **kwds: Any,
    ) -> TRequest:
        if index >= len(middlewares):
            return request

        async def next_call(request: TRequest) -> TRequest:
            return await self.process_middlewares(
                request, middlewares, index + 1, *args, **kwds
            )

        return await self._call_stage(
            request, middlewares[index], next_call, *args, **kwds
        )
