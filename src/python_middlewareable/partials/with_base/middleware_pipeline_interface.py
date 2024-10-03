from typing import Any, Optional, Protocol, Self
from thecodecrate_pipeline import PipelineInterface, T_in, T_out

from .types import MiddlewareNextCall
from .middleware_stage_interface import MiddlewareStageInterface
from .middleware_callable import MiddlewareCallable


class MiddlewarePipelineInterface(
    MiddlewareStageInterface[T_in, T_out],
    PipelineInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    async def __call__(
        self,
        payload: T_in,
        next_call: Optional[MiddlewareNextCall] = None,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    def pipe(self, stage: MiddlewareCallable) -> Self: ...
