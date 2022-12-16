from os import system
import subprocess
import sys
from multiprocessing import Pool
from functools import reduce
from time import perf_counter

inputs = [(5, 5, './tmp/images/LYO6Xq3RZ3gy.png')]

avg_exec_times_par = {}
avg_exec_times_seq = {}

def thread_fib(fib):
    return subprocess.check_output('./hey_linux_amd64 -n 1000 -m POST -d {} http://127.0.0.1:8080/function/fibonacci'.format(fib), shell=True).decode(sys.stdout.encoding)

def thread_matmul(matmul):
    return subprocess.check_output('./hey_linux_amd64 -n 1000 -m POST -d {} http://127.0.0.1:8080/function/matmul'.format(matmul), shell=True).decode(sys.stdout.encoding)

def thread_file(fileapi):
    return subprocess.check_output('./hey_linux_amd64 -n 1000 -m POST -D {} http://127.0.0.1:8080/function/file'.format(fileapi), shell=True).decode(sys.stdout.encoding)

def add_value_to_dict(value, dict):
    if (value < dict["min"]):
        dict["min"] = value
    if (value > dict["max"]):
        dict["max"] = value
    dict["avg"] += value

fib_results = open("fib_results.txt", "a")
matmul_results = open("matmul_results.txt", "a")
file_results = open("file_results.txt", "a")

print("Running sequential test...")
for fib, matmul, fileapi in inputs:
    avg_exec_times_seq.setdefault((fib, matmul, fileapi), {'min': float('inf'), 'max': -1, 'avg': 0})

    for i in range(5):
        fib_results.write("--- RUN SEQ {} ---\n\n".format(i))
        matmul_results.write("--- RUN SEQ {} ---\n\n".format(i))
        file_results.write("--- RUN SEQ {} ---\n\n".format(i))

        start = perf_counter()
        hey_output_fib = thread_fib(fib)
        hey_output_matmul = thread_matmul(matmul)
        hey_output_file = thread_file(fileapi)

        fib_results.write(hey_output_fib)
        matmul_results.write(hey_output_matmul)
        file_results.write(hey_output_file)

        add_value_to_dict(perf_counter() - start, avg_exec_times_seq[(fib, matmul, fileapi)])

    avg_exec_times_seq[(fib, matmul, fileapi)]["avg"] /= 5

print("Results:")
print(avg_exec_times_seq)

print("Running parallel test...")
for fib, matmul, fileapi in inputs:
    avg_exec_times_par.setdefault((fib, matmul, fileapi), {'min': float('inf'), 'max': -1, 'avg': 0})


    for i in range(5):
        fib_results.write("--- RUN PAR {} ---\n\n".format(i))
        matmul_results.write("--- RUN PAR {} ---\n\n".format(i))
        file_results.write("--- RUN PAR {} ---\n\n".format(i))
        start = perf_counter()


        pool = Pool(3)
        result_fib = pool.apply_async(thread_fib, args=(fib,))
        result_matmul = pool.apply_async(thread_matmul, args=(matmul,))
        result_file = pool.apply_async(thread_file, args=(fileapi,))

        pool.close()
        pool.join()

        hey_output_fib = result_fib.get()
        hey_output_matmul = result_matmul.get()
        hey_output_file = result_file.get()

        fib_results.write(hey_output_fib)
        matmul_results.write(hey_output_matmul)
        file_results.write(hey_output_file)

        add_value_to_dict(perf_counter() - start, avg_exec_times_par[(fib, matmul, fileapi)])

    avg_exec_times_par[(fib, matmul, fileapi)]["avg"] /= 5

print("Results:")
print(avg_exec_times_par)

fib_results.close()
matmul_results.close()
file_results.close()