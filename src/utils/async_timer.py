import functools
import time
from collections.abc import Callable
from collections.abc import Coroutine
from typing import ParamSpec
from typing import TypeVar

P = ParamSpec("P")
Y = TypeVar("Y")
S = TypeVar("S")
R = TypeVar("R")


def async_timed(
    func: Callable[P, Coroutine[Y, S, R]]
) -> Callable[P, Coroutine[Y, S, R]]:
    @functools.wraps(func)
    async def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"starting {func} with args {args} {kwargs}")
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            total = end - start
            print(f"finished {func} in {total:.4f} second(s)")

    return wrapped
