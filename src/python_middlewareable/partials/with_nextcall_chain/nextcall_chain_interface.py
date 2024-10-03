from typing import Any, Protocol
from thecodecrate_pipeline.support.has_call_async import (  # type: ignore
    HasCallAsyncInterface,
)

from ..with_base.types import MiddlewareNextCall
from ..with_base.middleware_callable import MiddlewareCallable


class NextcallChainInterface(
    HasCallAsyncInterface,
    Protocol,
):
    def __init__(self, stages: tuple[MiddlewareCallable, ...]) -> None: ...

    def get_nextcall(self) -> MiddlewareNextCall: ...

    def _build(
        self, stages: tuple[MiddlewareCallable, ...]
    ) -> MiddlewareNextCall: ...

    async def _default_next(
        self, payload: Any, *args: Any, **kwargs: Any
    ) -> Any: ...

    def _make_nextcall(
        self,
        stage: MiddlewareCallable,
        next_call: MiddlewareNextCall,
    ) -> MiddlewareNextCall: ...

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        stage: MiddlewareCallable,
        payload: Any,
        *args: Any,
        **kwds: Any,
    ) -> Any: ...
