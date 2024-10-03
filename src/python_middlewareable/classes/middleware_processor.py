from thecodecrate_pipeline import T_in, T_out

from .middleware_processor_interface import (
    MiddlewareProcessorInterface as ImplementsMiddlewareProcessorInterface,
)
from ..partials.with_nextcall_chain.middleware_processor_mixin import (
    MiddlewareProcessorMixin as WithProcessorChain,
)
from ..partials.with_base.middleware_processor import (
    MiddlewareProcessor as WithBase,
)
from ..partials.with_nextcall_chain_cached.middleware_processor_mixin import (  # noqa
    MiddlewareProcessorMixin as WithProcessorChainCached,
)


class MiddlewareProcessor(
    WithProcessorChainCached[T_in, T_out],
    WithProcessorChain[T_in, T_out],
    WithBase[T_in, T_out],
    ImplementsMiddlewareProcessorInterface[T_in, T_out],
):
    pass
