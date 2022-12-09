from multiprocessing import Manager
import multiprocessing as mp
import os
from random import sample


def thread_wrapper():
    os.system('for f in ./images/*.*; do curl -sS -o result http://127.0.0.1:8080/function/file -d @$f && echo executing file: $f; done')


# limit number of images in set
files = os.listdir('./images')

if len(files) > 100:
    for file in sample(files, 90):
        os.remove('./images/' + file)

manager = Manager()
pool = mp.Pool(12)

for _ in range(12):
    pool.apply_async(thread_wrapper)

pool.close()
pool.join()