import asyncio

from utils import async_timed


@async_timed
async def cpu_bound_work() -> int:
    counter = 0
    for _ in range(100_000_000):
        counter += 1
    return counter


async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
