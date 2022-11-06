import asyncio

from utils import async_timed
from utils import delay


@async_timed
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed
async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))

    await task_one
    await task_two
    await delay_task


if __name__ == "__main__":
    asyncio.run(main())
