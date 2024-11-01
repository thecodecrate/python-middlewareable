from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..with_base.middleware_processor_interface import (
    MiddlewareProcessorInterface as WithBaseInterface,
)


class MiddlewareProcessorInterfaceMixin(
    WithBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
