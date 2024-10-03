from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..partials.with_base.middleware_pipeline_interface import (
    MiddlewarePipelineInterface as WithMiddlewarePipelineBaseInterface,
)


class MiddlewarePipelineInterface(
    WithMiddlewarePipelineBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
