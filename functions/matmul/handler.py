import random
import time

def handle(req):
    try:
        n = int(req)
        if (n < 0):
            raise ValueError()
    except ValueError:
        print("Please provide a valid n > 0 as input")
        
    else: 
        start = time.time()
        A = [random.choices(range(0, 10), k=n) for _ in range(n)]
        B = [random.choices(range(0, 10), k=n) for _ in range(n)]
        end = time.time()
        fill = end - start

        if len(A) == len(B[0]):
            start = time.time()
            C = [[sum(a * b for a, b in zip(A_row, B_col))
                for B_col in zip(*B)]
                for A_row in A]
            end = time.time()
            calc = end - start
        
        else:
            return "Matrices can not be multiplied."

        return [fill, calc]