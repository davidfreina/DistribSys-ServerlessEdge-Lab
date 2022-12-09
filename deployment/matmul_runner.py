from multiprocessing import Manager
import multiprocessing as mp
import os


def thread_wrapper():
    for i in range(50, 450, 50):
        os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))
        # os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))


manager = Manager()
pool = mp.Pool(8)

for _ in range(8):
    pool.apply_async(thread_wrapper)

pool.close()
pool.join()