import os
import random
import requests
import subprocess
from time import perf_counter
import struct
import sys

start = 5
end = 45
step = 5

avg_exec_times = {}

for fib in range(start, end, step):
    avg_exec_times.setdefault(fib, 0)
    for _ in range(5):
        start = perf_counter()
        time = subprocess.check_output('curl -w "%{{time_total}}" -o NUL -sS http://127.0.0.1:8080/function/fibonacci -d {}'.format(fib), shell=True).decode(sys.stdout.encoding)
        avg_exec_times[fib] += float(time)
    avg_exec_times[fib] = avg_exec_times[fib] / 5

print(avg_exec_times)