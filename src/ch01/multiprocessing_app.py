import multiprocessing
import os


def hello_from_process() -> None:
    print(f"Hello from child process {os.getgid()}!")


if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Hello from parent process {os.getgid()}!")

    hello_process.join()
