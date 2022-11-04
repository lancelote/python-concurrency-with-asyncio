import asyncio


def main() -> None:
    my_future: asyncio.Future[int] = asyncio.Future()
    print(f"Is my future done? {my_future.done()}")

    my_future.set_result(42)

    print(f"Is my future done? {my_future.done()}")
    print(f"What is my future result? {my_future.result()}")


if __name__ == "__main__":
    main()
