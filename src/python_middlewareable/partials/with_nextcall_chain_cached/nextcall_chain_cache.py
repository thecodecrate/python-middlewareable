from typing import Optional, Self
from thecodecrate_pipeline.support.clonable import Clonable  # type: ignore


from .nextcall_chain_cache_interface import NextcallChainCacheInterface
from ..with_base.middleware_callable import MiddlewareCallable
from ..with_nextcall_chain.nextcall_chain import NextcallChain


class NextcallChainCache(
    Clonable,
    NextcallChainCacheInterface,
):
    _cached_chain: Optional[NextcallChain]
    _cached_hash: Optional[int]

    def __init__(self) -> None:
        self._cached_chain = None

        self._cached_hash = None

    def with_stages(self, stages: tuple[MiddlewareCallable, ...]) -> Self:
        stages_hash = hash(stages)

        if self._cached_hash != stages_hash:
            return self.clone(
                {
                    "_cached_chain": NextcallChain(stages=stages),
                    "_cached_hash": stages_hash,
                }
            )

        return self

    def get_chain(self) -> NextcallChain:
        assert self._cached_chain is not None

        return self._cached_chain
