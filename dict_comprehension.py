print('Example-1:')

dict1 = {i:i+10 for i in range(10)}
print(dict1)

print()

print('Example-2:')

dict2 = {'Rakib': 28, 'Sakib': 32, 'Akib': 35}
dict3 = {k:v for k, v in dict2.items() if v%2==0}
dict4 = {k:v for k, v in dict2.items() if v%2==0 if v>30}
print(dict3)
print(dict4)

print()

print('Example-3:')

dict5 = {'Rakib': 28, 'Sakib': 32, 'Akib': 65}
dict6 = {k: ('Old' if v>=50 else 'Young') for k, v in dict5.items()}
print(dict6)

print()

print('Example-4:')

dict7 = {k1 : {k2 : k1*k2} for k2 in range(6) for k1 in range(5)}
print(dict7)

print()