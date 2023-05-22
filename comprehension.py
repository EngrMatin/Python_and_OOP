numbers = [12, 45, 23, 65, 89, 78, 11, 82]

odd_nums = []
for x in numbers:
    if x%2==1 and x%5==0:
        odd_nums.append(x)

print(odd_nums)

# equivalent 1 line loop expression:
odd_numbers = [x for x in numbers if x%2==1 if x%5==0]
print(odd_numbers)