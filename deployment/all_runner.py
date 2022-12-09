from multiprocessing import Manager
import multiprocessing as mp
import os
import random


def file_wrapper():
    os.system('for f in ./images/*.*; do curl -sS -o result http://127.0.0.1:8080/function/file -d @$f && echo executing file: $f; done')

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

def thread_wrapper4():
    for i in range(50, 450, 50):
        os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))

def thread_wrapper5():
    for i in range(450, 450, -50):
        os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))



# limit number of images in set
files = os.listdir('./images')

if len(files) > 100:
    for file in random.sample(files, 90):
        os.remove('./images/' + file)


manager = Manager()
pool = mp.Pool(18)

for _ in range(3):
    pool.apply_async(file_wrapper)
    pool.apply_async(thread_wrapper)
    pool.apply_async(thread_wrapper2)
    pool.apply_async(thread_wrapper3)
    pool.apply_async(thread_wrapper4)
    pool.apply_async(thread_wrapper5)

pool.close()
pool.join()