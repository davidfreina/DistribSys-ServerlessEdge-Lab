from time import time

def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

def handle(req):
    try:
        req = int(req)
        if (req < 0):
            raise ValueError()
    except ValueError:
        print("Please provide a valid integer > 0 as input")
    else:
        start = time()
        fib = rec_fib(req)
        print("n: {}, fib: {}, time: {}s".format(req, fib, time()-start))