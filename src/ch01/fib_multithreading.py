import threading
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


def fib_with_threads() -> None:
    thread_40 = threading.Thread(target=print_fib, args=(40,))
    thread_41 = threading.Thread(target=print_fib, args=(41,))

    thread_40.start()
    thread_41.start()

    thread_40.join()
    thread_41.join()


start = time.time()
fib_with_threads()
end = time.time()

print(f"Threads took {end - start:.4f} seconds.")
