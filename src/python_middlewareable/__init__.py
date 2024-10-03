from .classes.middleware_interface import MiddlewareInterface as Middleware
from .classes.middlewareable import Middlewareable
from .classes.types import MiddlewareNextCall, TRequest

# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.0.0"

__all__ = [
    # Core
    "Middleware",
    "Middlewareable",
    "MiddlewareNextCall",
    "TRequest",
]
