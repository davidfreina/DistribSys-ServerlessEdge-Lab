from multiprocessing import Manager
import multiprocessing as mp
import os
from random import sample


def file_wrapper():
    os.system('for f in ./images/*.*; do curl -sS -o result http://127.0.0.1:8080/function/file -d @$f && echo executing file: $f; done')

def matmul_wrapper():
    for i in range(50, 450, 50):
        os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))
        os.system('curl -sS http://127.0.0.1:8080/function/matmul -d {}'.format(i))

def fibonacci_wrapper():
    for i in range(20, 42):
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(i))
        os.system('curl -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(i))



# limit number of images in set
files = os.listdir('./images')

if len(files) > 100:
    for file in sample(files, 80):
        os.remove('./images/' + file)


manager = Manager()
pool = mp.Pool(10)

for _ in range(4):
    pool.apply_async(file_wrapper)
    pool.apply_async(matmul_wrapper)
    pool.apply_async(fibonacci_wrapper)

pool.close()
pool.join()