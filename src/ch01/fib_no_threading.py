import time


# Intentionally slow
def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) is {fib(number)}")


def fib_no_threads():
    print_fib(40)
    print_fib(41)


start = time.time()
fib_no_threads()
end = time.time()

print(f"Completed in {end - start:.4f} seconds.")
