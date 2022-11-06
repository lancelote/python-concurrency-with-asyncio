import asyncio

from utils import delay


def call_later() -> None:
    print("I'm being called in the future!")


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


if __name__ == "__main__":
    asyncio.run(main())
