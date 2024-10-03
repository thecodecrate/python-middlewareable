from typing import Generic
from thecodecrate_pipeline import Pipeline

from ..pipeline.middleware_pipeline import MiddlewarePipeline
from ..pipeline.middleware_processor import MiddlewareProcessor
from .types import TRequest


class Middlewareable(
    MiddlewarePipeline[TRequest],
    Pipeline[TRequest],
    Generic[TRequest],
):
    processor_class = MiddlewareProcessor
