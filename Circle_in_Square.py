from math import pi

t = int(input())
for i in range(t):
    r = float(input())

    ans = round((((2*r)**2)-(pi*r*r)), 2)

    print(f'Case {i+1}: {ans}')