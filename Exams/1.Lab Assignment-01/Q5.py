def create_list(dict):
    list1 = list(dict.items())
    
    list2 = []
    for i in list1:
        for t in i:
            list2.append(t)

    return list2

x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}  
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

print(create_list(x))
print(create_list(d))






