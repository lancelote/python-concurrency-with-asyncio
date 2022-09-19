async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


coroutine_result = coroutine_add_one(1)
function_result = add_one(1)

print(f"coroutine result is {coroutine_result} "
      f"with type {type(coroutine_result)}")
print(f"function result is {function_result} "
      f"with type {type(function_result)}")
