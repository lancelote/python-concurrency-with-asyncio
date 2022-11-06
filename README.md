# python-concurrency-with-asyncio

- My experiments and notes while reading "[Python Concurrency with asyncio][book]" book by [Matthew Fowler][author]
- [Code from the book][code]

## TOC

- [x] [Chapter 1: Getting to know asyncio](src/ch01)
  - [Bound operations](src/ch01/bound_operations.py)
  - [Processes and threads](src/ch01/processes_and_threads.py)
  - [Multithreaded application](src/ch01/multithreaded.py)
  - [Multiprocessing application](src/ch01/multiprocessing_app.py)
  - [Fibonacci with no threads](src/ch01/fib_no_threading.py)
  - [Naive Multithreading Fibonacci](src/ch01/fib_multithreading.py)
  - [Synchronously reading status](src/ch01/sync_read_status.py)
  - [Multithreaded status reading](src/ch01/multithreaded_status.py)
- [ ] [Chapter 2: asyncio basics](src/ch02)
  - [Compare functions and coroutines](src/ch02/compare_coro.py)
  - [Running a coroutine](src/ch02/running_a_coroutine.py)
  - [Using `async`](src/ch02/using_async.py)
  - [Long-running coroutines](src/ch02/long_running_coroutines.py)
  - [`delay` coroutine](src/utils/delay_functions.py)
  - [Running two coroutines](src/ch02/two_coroutines.py)
  - [Basic tasks](src/ch02/basic_tasks.py)
  - [Running multiple tasks](src/ch02/running_multiple_tasks.py)
  - [Running code while other operations](src/ch02/run_code_while_other.py)
  - [Canceling tasks](src/ch02/canceling_tasks.py)
  - [Setting a timeout](src/ch02/setting_timeout.py)
  - [Protecting from cancellation](src/ch02/protecting_from_cancel.py)
  - [Futures](src/ch02/futures.py)
  - [Awaiting a future](src/ch02/awaiting_a_future.py)
  - [Measure coroutine execution time with decorator](src/utils/async_timer.py)
  - [Timing a coroutine](src/ch02/timing_coroutine.py)
  - [Running CPU-bound code concurrently](src/ch02/cpu_concurrently.py)
  - [CPU-bound code with a sleep](src/ch02/cpu_bound_task.py)
  - [Incorrect work with blocking API](src/ch02/blocking_api_incorrect.py)
  - [Create event loop manually](src/ch02/create_event_loop.py)
  - [Get event loop](src/ch02/get_event_loop.py)
- [ ] Chapter 3: A first asyncio application
- [ ] Chapter 4: Concurrent web requests
- [ ] Chapter 5: Non-blocking database drivers
- [ ] Chapter 6: Handling CPU-bound work
- [ ] Chapter 7: Handling blocking work with threads
- [ ] Chapter 8: Streams
- [ ] Chapter 9: Web applications
- [ ] Chapter 10: Microservices
- [ ] Chapter 11: Synchronization
- [ ] Chapter 12: Asynchronous queues
- [ ] Chapter 13: Managing subprocesses
- [ ] Chapter 14: Advanced asyncio

[code]: https://github.com/concurrency-in-python-with-asyncio/concurrency-in-python-with-asyncio
[book]: https://www.manning.com/books/python-concurrency-with-asyncio
[author]: https://www.linkedin.com/in/matthew-fowler-5088609/
