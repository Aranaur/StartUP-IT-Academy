import concurrent.futures
import time


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


n_1 = 100
n_2 = 100

start = time.time()
factorial(n_1)
factorial(n_2)
end = time.time() - start

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread_executor:
        start_thread = time.time()
        number_1 = thread_executor.submit(factorial, n_1).result()
        number_2 = thread_executor.submit(factorial, n_2).result()
        end_thread = time.time() - start_thread

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as process_executor:
        start_process = time.time()
        number_1 = process_executor.submit(factorial, n_1).result()
        number_2 = process_executor.submit(factorial, n_2).result()
        end_process = time.time() - start_process

    end_dict = {
        'base': end,
        'thread': end_thread,
        'process': end_process
    }
    print(f'Best time has {min(end_dict, key=end_dict.get)} method with {end_dict[min(end_dict, key=end_dict.get)]} score')
