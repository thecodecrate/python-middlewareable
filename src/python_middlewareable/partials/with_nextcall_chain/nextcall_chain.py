from typing import Any, TypeVar
from thecodecrate_pipeline.support.has_call_async import (  # type: ignore
    HasCallAsync,
)

from .nextcall_chain_interface import NextcallChainInterface
from ..with_base.types import MiddlewareNextCall
from ..with_base.middleware_callable import MiddlewareCallable

TCallableReturn = TypeVar("TCallableReturn", infer_variance=True)


class NextcallChain(
    HasCallAsync,
    NextcallChainInterface,
):
    _nextcall: MiddlewareNextCall

    def __init__(self, stages: tuple[MiddlewareCallable, ...]) -> None:
        self._nextcall = self._build(stages=stages)

    def get_nextcall(self) -> MiddlewareNextCall:
        return self._nextcall

    def _build(
        self, stages: tuple[MiddlewareCallable, ...]
    ) -> MiddlewareNextCall:
        next_call = self._default_next

        for stage in reversed(stages):
            next_call = self._make_nextcall(stage=stage, next_call=next_call)

        return next_call

    async def _default_next(
        self, payload: Any, *args: Any, **kwargs: Any
    ) -> Any:
        return payload

    def _make_nextcall(
        self,
        stage: MiddlewareCallable,
        next_call: MiddlewareNextCall,
    ) -> MiddlewareNextCall:
        async def new_nextcall(
            payload: Any,
            *args: Any,
            **kwargs: Any,
        ) -> Any:
            return await self._call(
                stage=stage,
                payload=payload,
                next_call=next_call,
                *args,
                **kwargs,
            )

        return new_nextcall

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        stage: MiddlewareCallable,
        payload: Any,
        *args: Any,
        **kwds: Any,
    ) -> Any:
        return await super()._call(stage, payload, *args, **kwds)
