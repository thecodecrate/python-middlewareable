from thecodecrate_pipeline import T_in, T_out

from .middleware_stage_interface import (
    MiddlewareStageInterface as ImplementsMiddlewareStageInterface,
)
from ..partials.with_base.middleware_stage import (
    MiddlewareStage as WithMiddlewareStageBaseConcern,
)


class MiddlewareStage(
    WithMiddlewareStageBaseConcern[T_in, T_out],
    ImplementsMiddlewareStageInterface[T_in, T_out],
):
    pass
