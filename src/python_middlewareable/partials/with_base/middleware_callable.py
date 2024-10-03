from typing import Any, Awaitable, Protocol
from thecodecrate_pipeline import StageCallable, T_in, T_out

from .types import MiddlewareNextCall


class MiddlewareCallable(
    StageCallable[T_in, T_out],
    Protocol,
):
    def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional parameter
        next_call: MiddlewareNextCall,
        *args: Any,
        **kwds: Any,
    ) -> T_out | Awaitable[T_out]: ...
