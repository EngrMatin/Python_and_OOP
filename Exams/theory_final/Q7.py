lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sliced_list = lst[2:20:3]
print(sliced_list)


# Alternative method:
new_list = []
for x in lst:
    if x%3 == 0:
        new_list.append(x)
        
print(new_list)