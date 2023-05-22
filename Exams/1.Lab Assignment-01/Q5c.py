def create_list(dict):
    list1 = []
    
    for key, value in dict.items():
        list1.extend([key, value])

    return list1

x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}  
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

print(create_list(x))
print(create_list(d))






