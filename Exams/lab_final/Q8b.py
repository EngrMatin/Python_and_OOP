def max(lst, n):                      # ([4, 12, 3, 14, 5]  5)    ([12, 3, 14, 5]  5)   ([3, 14, 5]  12)   ([14, 5]  12)   ([5]  14)   ([]  14)
    if lst == []:
        return n                      #                                                                                                     14                                                                                                      
    # elif lst[0] > n:                  # 4>5? False                 12>5? True            3>5? False        14>12? True     5>14? False
    #     return max(lst[1: ], lst[0])  #                            ([3, 14, 5]  12)                        ([5]  14)
    else:
        # return max(lst[1: ], n)       # ([12, 3, 14, 5]  5)                              ([14, 5]   12)                    ([]  14)
        mx = 0
        for x in lst:
            if mx < x:
                mx = x
        return mx

lst1 = [4, 12, 3, 14, 5]
n = len(lst1)

print(max(lst1, n))
