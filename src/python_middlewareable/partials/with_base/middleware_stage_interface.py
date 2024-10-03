from abc import abstractmethod
from typing import Any, Protocol
from thecodecrate_pipeline import StageInterface, T_in, T_out

from .types import MiddlewareNextCall


class MiddlewareStageInterface(
    StageInterface[T_in, T_out],
    Protocol,
):
    @abstractmethod
    async def handle(
        self,
        request: T_in,
        next_call: MiddlewareNextCall,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    # inherited from StageInterface
    async def __call__(
        self,
        payload: T_in,
        next_call: MiddlewareNextCall,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
