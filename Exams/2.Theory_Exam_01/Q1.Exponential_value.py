import math

def exp(a, n):
    # return pow(a, n)
    return a**n

a, n = [int(x) for x in input("Enter two values: ").split()]
# a, n = input("Enter two values: ").split()
# a = int(a)
# n = int(n)
result = exp(a, n)
print(f"{a} to the power {n} is {result}")

