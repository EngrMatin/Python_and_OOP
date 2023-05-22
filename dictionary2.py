dict1 = {'rahim':12000, 'karim':20000}
print(dict1['rahim'])           # 12000
print(dict1.get('rahim'))       # 12000

# print(dict1['halim'])                 # error
print(dict1.get('halim'))               # None
print(dict1.get('halim', False))        # False


child1 = {
    'name': 'jack',
    'year': 2002
}

child2 = {
    'name': 'emilia',
    'year': 2004
}

child3 = {
    'name': 'tom',
    'year': 2007
}

myFamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(myFamily)    # {'child1': {'name': 'jack', 'year': 2002}, 'child2': {'name': 'emilia', 'year': 2004}, 'child3': {'name': 'tom', 'year': 2007}}
print(myFamily['child2']['year'])     # 2004
print(myFamily.get('child2', False).get('year', False))     # 2004
print(myFamily.get('child2', False).get('age', False))      # False
print(myFamily.get('child4', False))     # False
# print(myFamily.get('child4', False).get('year', False))     # error



