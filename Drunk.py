t = int(input())
for i in range(t):
    n = int(input())
    flag = True
    for j in range(n):
        a, b = input().split(' ')
        
        if a=='wine' or b!='wine':
            flag = False

    if flag == True:
        print(f'Case {i+1}: Yes')
    else:
        print(f'Case {i+1}: No')