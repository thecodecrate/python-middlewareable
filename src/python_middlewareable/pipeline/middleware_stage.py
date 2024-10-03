from abc import abstractmethod
from typing import Any, Protocol
from thecodecrate_pipeline import (
    StageInterface,
)

from ..classes.types import TRequest, MiddlewareNextCall


class MiddlewareStage(
    StageInterface[TRequest],
    Protocol[TRequest],
):
    # inherited from StageInterface
    async def __call__(
        self,
        payload: TRequest,
        next_call: MiddlewareNextCall[TRequest],
        *args: Any,
        **kwds: Any,
    ) -> TRequest:
        return await self.handle(payload, next_call, *args, **kwds)

    ###
    # --- User implements middleware logic here ---
    # - "args and kwds" allows extend the class with custom args
    ###
    @abstractmethod
    async def handle(
        self,
        request: TRequest,
        next_call: MiddlewareNextCall[TRequest],
        *args: Any,
        **kwds: Any,
    ) -> TRequest:
        return await next_call(request)
