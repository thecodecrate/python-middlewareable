from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..partials.with_nextcall_chain.middleware_processor_interface_mixin import (  # noqa
    MiddlewareProcessorInterfaceMixin as WithProcessorChainInterface,
)
from ..partials.with_base.middleware_processor_interface import (
    MiddlewareProcessorInterface as WithBaseInterface,
)
from ..partials.with_nextcall_chain_cached.middleware_processor_interface_mixin import (  # noqa
    MiddlewareProcessorInterfaceMixin as WithProcessorChainCachedInterface,
)


class MiddlewareProcessorInterface(
    WithProcessorChainCachedInterface[T_in, T_out],
    WithProcessorChainInterface[T_in, T_out],
    WithBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
