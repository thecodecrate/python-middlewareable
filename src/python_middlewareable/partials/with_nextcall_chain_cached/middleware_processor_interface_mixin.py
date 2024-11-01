from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..with_nextcall_chain.middleware_processor_interface_mixin import (
    MiddlewareProcessorInterfaceMixin as WithProcessorBaseInterface,
)
from ..with_base.middleware_processor_interface import (
    MiddlewareProcessorInterface as WithBaseInterface,
)


class MiddlewareProcessorInterfaceMixin(
    WithProcessorBaseInterface[T_in, T_out],
    WithBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
