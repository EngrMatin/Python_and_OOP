testCase = int(input())
for i in range(testCase):

    a, b = map(int, input().split())

    if a%b==0:
        print(f'Case {i+1}: divisible')
    else:
        print(f'Case {i+1}: not divisible')