from typing import Any
from thecodecrate_pipeline import Stage, T_in, T_out

from .types import MiddlewareNextCall
from .middleware_stage_interface import MiddlewareStageInterface


class MiddlewareStage(
    Stage[T_in, T_out],
    MiddlewareStageInterface,
):
    async def handle(
        self,
        request: T_in,
        next_call: MiddlewareNextCall,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await next_call(request, *args, **kwds)

    # inherited from StageInterface
    async def __call__(
        self,
        payload: T_in,
        next_call: MiddlewareNextCall,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await self.handle(payload, next_call, *args, **kwds)
