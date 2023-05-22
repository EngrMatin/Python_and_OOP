from math import pi

def outer_function():
    pi = 6.66

    def inner_function():
        pi = 5.55
        print(f'The value of ENCLOSED pi is {pi}')
    
    inner_function()
    print(f'The value of LOCAL pi is {pi}')


print(f'The value of BUILT-IN pi is {pi}')
pi = 3.33
print(f'The value of GLOBAL pi is {pi}')
outer_function()