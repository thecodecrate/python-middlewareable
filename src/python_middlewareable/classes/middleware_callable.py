from typing import Protocol
from thecodecrate_pipeline import T_in, T_out

from ..partials.with_base.middleware_callable import (
    MiddlewareCallable as WithMiddlewareCallableBase,
)


class MiddlewareCallable(
    WithMiddlewareCallableBase[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
