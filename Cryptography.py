prime_nums = []

for num in range(2, 15000):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_nums.append(num)

#print(prime_nums) 

t = int(input())

position_list = []

for i in range(t):
    n = int(input())
    position_list.append(n)
#print(position_list)
for pos in position_list:
    #print(pos)
    print(prime_nums[pos-1])