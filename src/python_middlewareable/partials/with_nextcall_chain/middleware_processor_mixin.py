from typing import Any, cast
from thecodecrate_pipeline import T_in, T_out

from .nextcall_chain import NextcallChain
from ..with_base.middleware_callable import MiddlewareCallable
from .middleware_processor_interface_mixin import (
    MiddlewareProcessorInterfaceMixin as ImplementsMiddlewareProcessorInterface,  # noqa
)


class MiddlewareProcessorMixin(
    ImplementsMiddlewareProcessorInterface[T_in, T_out],
):
    async def process(
        self,
        payload: T_in,
        stages: tuple[MiddlewareCallable, ...],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        nextcall = NextcallChain(stages=stages).get_nextcall()

        result = await nextcall(payload, *args, **kwds)

        return cast(T_out, result)
