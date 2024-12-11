from functools import lru_cache
import time

# def main(n):
#     memo = {}
#     start_time = time.time()

def fib(n, memo = None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]


    # ans = fib(n)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # return ans, elapsed_time

# ans, elapsed_time = main(999)
ans = fib(999)
print(ans)
# print(f"Execution time: {elapsed_time:.6f}")