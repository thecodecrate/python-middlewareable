from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..partials.with_base.middleware_stage_interface import (
    MiddlewareStageInterface as WithMiddlewareStageBaseInterface,
)


class MiddlewareStageInterface(
    WithMiddlewareStageBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
