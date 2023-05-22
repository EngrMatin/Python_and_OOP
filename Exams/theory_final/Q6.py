n = int(input('Enter the number of lines: '))

for i in range(1, n+1):
    for j in range(1, n+1):
        if j<i:
            j=j+1
        elif i==j:
            j=1
        print(j, end=' ')
    print()


'''
1 2 3 4 5
2 1 3 4 5
2 3 1 4 5
2 3 4 1 5
2 3 4 5 1

'''