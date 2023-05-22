def mylen(lst, n):                      # ([4, 12, 3, 14, 5]  5)  ([12, 3, 14, 5]  6)   ([5]  9)   ([]  10)  
    if lst == []:                       # False                    False                False       True
        return n                        #                                                               10
    else:
        #return mylen(lst[1: ], n+1)     # ([12, 3, 14, 5]  6)     ([3, 14, 5]  7)       ([]  10)
        for x in lst:
            n = n+1
        return n

lst1 = [4, 12, 3, 14, 5]
n = len(lst1)

print(mylen(lst1, n))