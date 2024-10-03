from typing import Protocol, Self
from thecodecrate_pipeline.support.clonable import (  # type: ignore
    ClonableInterface,
)

from ..with_base.middleware_callable import MiddlewareCallable
from ..with_nextcall_chain.nextcall_chain import NextcallChain


class NextcallChainCacheInterface(
    ClonableInterface,
    Protocol,
):
    def __init__(self) -> None: ...

    def with_stages(self, stages: tuple[MiddlewareCallable, ...]) -> Self: ...

    def get_chain(self) -> NextcallChain: ...
