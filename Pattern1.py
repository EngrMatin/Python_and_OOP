rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print()

for i in range(rows):
    for j in range(i):
        print(j, end=' ')
    print()

for i in range(rows):
    for j in range(i):
        print('*', end=' ')
    print()