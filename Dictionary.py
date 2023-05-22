dict1 = {'physics': 65, 'chemistry': 70, 'math': 88}
print(dict1)

dict1['physics'] = 75
dict1['english'] = 85
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
for key, value in dict1.items():
    print(f'{key} : {value}')

for x in dict1:
    print(x)         # will return keys

for x in dict1:
    val = dict1[x]
    print(val)

print("Sum of the Dictionary: ", sum(dict1.values()))

sum = 0
for x in dict1.values():
    sum += x
print(sum)

for a, b in dict1.items():
    print(a, b)
    
print(dict1.clear())

dict1.clear()
print(dict1)