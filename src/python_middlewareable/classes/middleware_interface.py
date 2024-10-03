from typing import Protocol
from thecodecrate_pipeline import (
    StageInterface,
)

from .types import TRequest
from ..pipeline.middleware_stage import MiddlewareStage


class MiddlewareInterface(
    MiddlewareStage[TRequest],
    StageInterface[TRequest],
    Protocol[TRequest],
):
    pass
