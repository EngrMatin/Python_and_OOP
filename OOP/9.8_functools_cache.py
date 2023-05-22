import time
from functools import cache

# Fibonacci series: 1,1,2,3,5,8,13,21,34,55, . . . . . .

@cache
def fib(n):
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)

start = time.time()
for i in range(40):
    print(i, fib(i))
end = time.time()
mili_secs = (end - start)*1000
print('Time taken: ', mili_secs)      # Time taken:  53896.97551727295 ms (without cache)
                                      # Time taken:  0.99945068359375



