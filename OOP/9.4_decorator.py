
def timer(func):
    def inner():
        print('Time start')
        func()
        print('Time end')
    return inner

def get_factorial():
    print('Factorial')

timer(get_factorial)()
print('\n')



def timer(func):
    def inner():
        print('Time start')
        func()
        print('Time end')
    return inner

@timer
def get_factorial():
    print('Factorial')

get_factorial()
print('\n')


import math
import time

def timer(func):
    def inner(*args, **kwargs):
        print('Time start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time end. Total time taken: {end-start}')
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}')

get_factorial(50)

