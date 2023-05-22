rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
seats = [[chr(j+65)+str(i) for i in range(cols)] for j in range(rows)]
#print(seats)

print('*'*70)
print()
for x in seats:
    for y in x:
        print(y, end="\t\t")
    print()
print()
print('*'*70)

seats[2][1] = 'X'
seats[2][3] = 'XX'

print('*'*70)
print()
for x in seats:
    for y in x:
        print(y, end="\t\t")
    print()
print()
print('*'*70)