from thecodecrate_pipeline import T_in, T_out

from .middleware_processor import MiddlewareProcessor
from .middleware_pipeline_interface import (
    MiddlewarePipelineInterface as ImplementsMiddlewarePipelineInterface,
)
from ..partials.with_base.middleware_pipeline import (
    MiddlewarePipeline as WithMiddlewarePipelineBaseConcern,
)


class MiddlewarePipeline(
    WithMiddlewarePipelineBaseConcern[T_in, T_out],
    ImplementsMiddlewarePipelineInterface[T_in, T_out],
):
    processor_class = MiddlewareProcessor
