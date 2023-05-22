print('Example-1:')

list1 = ['I', 'Love', 'Bangladesh']
list2 = [x.upper() for x in list1]
print(list2)

print()

print('Example-2:')

list3 = [i for i in range(1, 10)]
list4 = list(range(1, 10))
print(list3)
print(list4)

print()

print('Example-3:')

str = 'Bangladesh'

list5 = list(str)
print(list5)

list6 = [i for i in str]
print(list6)

print()

print('Example-4:')

list7 = [i for i in range(1, 20) if i%2==0]
print(list7)

print()

print('Example-5:')

list8 = [i for i in range(100) if i%3==0 if i%5==0]
print(list8)

print()

print('Example-6:')

list9 = ['Even' if x%2==0 else 'Odd' for x in range(20)]
print(list9)

print()

print('Example-7:')

list10 = [(x,y) for x in [1,2,3,7,8,9] for y in [2,3,4,8,9,10] if x!=y]
print(list10)

print()
