from typing import Any, cast
from thecodecrate_pipeline import T_in, T_out

from .nextcall_chain_cache import NextcallChainCache
from ..with_base.middleware_callable import MiddlewareCallable
from .middleware_processor_interface_mixin import (
    MiddlewareProcessorInterfaceMixin as ImplementsMiddlewareProcessorInterface,  # noqa
)


class MiddlewareProcessorMixin(
    ImplementsMiddlewareProcessorInterface[T_in, T_out],
):
    _cache: NextcallChainCache

    def __init__(self, *args: Any, **kwds: Any):
        self._cache = NextcallChainCache()

    async def process(
        self,
        payload: T_in,
        stages: tuple[MiddlewareCallable, ...],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        # using local variable for thread safety
        cache = self._cache.with_stages(tuple(stages))

        self._cache = cache

        nextcall = cache.get_chain().get_nextcall()

        result = await nextcall(payload, *args, **kwds)

        return cast(T_out, result)
