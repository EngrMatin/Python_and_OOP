x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}  
# d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

list1 = list(x.items())
# list1 = list(d.items())

list2 = []
for i in list1:
    for t in i:
        list2.append(t)

print(list2)