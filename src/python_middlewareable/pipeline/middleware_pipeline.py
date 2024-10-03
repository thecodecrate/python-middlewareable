from typing import Any, Protocol, Self
from thecodecrate_pipeline import (
    PipelineInterface,
)

from .middleware_callable import MiddlewareCallable
from ..classes.middleware_interface import MiddlewareInterface
from ..classes.types import TRequest


class MiddlewarePipeline(
    PipelineInterface[TRequest],
    Protocol[TRequest],
):
    middlewares: list[type[MiddlewareInterface[TRequest]]] = []

    middleware_instances: list[MiddlewareCallable[TRequest]] = []

    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self._instantiate_middlewares()

    def _instantiate_middlewares(self) -> None:
        self.middleware_instances = [
            middleware() for middleware in self.middlewares
        ]

    def get_items(self) -> list[MiddlewareCallable[TRequest]]:
        return self.middleware_instances

    def set_items(self, items: list[MiddlewareCallable[TRequest]]) -> Self:
        self.middleware_instances = items

        return self

    def add(self, middleware: MiddlewareCallable[TRequest]) -> Self:
        return self.add_item(middleware)
