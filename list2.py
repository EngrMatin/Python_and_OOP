list1 = [1,2,3,2,5]
list2 = [10,20,30,20,50]

print(list1.count(2))    # 2
print(list1 + list2)     # [1, 2, 3, 2, 5, 10, 20, 30, 20, 50]

list1.extend(list2)
print(list1)             # [1, 2, 3, 2, 5, 10, 20, 30, 20, 50]

list3 = [1,2,3,4,[5,6,7,[8,9,[10,[11,12]]]]]
print(list3[4][3][2][1][0])        # 11
print(list3[4][3][2][1][1])        # 12

list3[4][3][2][1][0] = list3[4][3][2][1][0] * 3
print(list3)            # [1, 2, 3, 4, [5, 6, 7, [8, 9, [10, [33, 12]]]]]

list3.append(100)
print(list3)            # [1, 2, 3, 4, [5, 6, 7, [8, 9, [10, [33, 12]]]], 100]

print(4 in list3)       # True
print(100 in list3)     # True
print(300 in list3)     # False
print(8 in list3)       # False  Here, 8 is not an item of the main list. It is an item of the nested nested list.



