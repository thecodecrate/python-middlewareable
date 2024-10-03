from typing import Any, Optional, Self
from thecodecrate_pipeline import Pipeline, T_in, T_out

from .types import MiddlewareNextCall
from .middleware_stage import MiddlewareStage
from .middleware_callable import MiddlewareCallable
from .middleware_pipeline_interface import MiddlewarePipelineInterface


class MiddlewarePipeline(
    MiddlewareStage[T_in, T_out],
    Pipeline[T_in, T_out],
    MiddlewarePipelineInterface[T_in, T_out],
):
    async def __call__(
        self,
        payload: T_in,
        next_call: Optional[MiddlewareNextCall] = None,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        result = await self.process(payload=payload, *args, **kwds)

        if next_call:
            return await next_call(result, *args, **kwds)

        return result

    def pipe(self, stage: MiddlewareCallable) -> Self:
        return super().pipe(stage)
