def sum_odd(n, total):                   # (10,55)  (9,55)  (7,64)  (5,71)  (3,76)  (1,79)
    if n == 1:
        return total                                                                 # 79
    # elif n%2 == 0:
    #     return sum_odd(n-1, total)       # (9,55)
    else:
        # return sum_odd(n-2, total+n)     # (7,64)  (5,71)  (3,76)  (1,79)
        for i in range(2, n+1):
            if i%2 != 0:
                total = total+i
        return total
            

l1 = [10, 21, 33, 9, 55, 8, 77, 8, 99, 10]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(l1)
total = sum(l1)

print(sum_odd(n, total))