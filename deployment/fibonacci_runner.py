from multiprocessing import Manager
import multiprocessing as mp
import os
import random


def thread_wrapper():
    for i in range(5, 37):
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(i))
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format((i + 5) % 37))


def thread_wrapper2():
    for i in range(37, 5, -1):
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(i))
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format((i + 5) % 37))

def thread_wrapper3():
    for _ in range(50):
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(random.randint(5, 37)))


manager = Manager()
pool = mp.Pool(18)

for _ in range(3):
    pool.apply_async(thread_wrapper2)
    pool.apply_async(thread_wrapper)
    pool.apply_async(thread_wrapper3)
    pool.apply_async(thread_wrapper2)
    pool.apply_async(thread_wrapper)
    pool.apply_async(thread_wrapper3)


pool.close()
pool.join()