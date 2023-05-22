list1 = [11, 22, 33, 22, 33, 11, 44, 55, 22, 11]
print(list1)

set1 = set(list1)
print(set1)          # No duplicate, No order

set2 = {1, 2, 3, 5, 3, 4, 5}
print(set2)

set1.add(66)
print(set1)

set1.add(55)
print(set1)

set1.remove(66)
print(set1)

NoOfItems = len(set1)
print("No of Items: ", NoOfItems)

print("Sum of the list: ", sum(set1))

total = 0
for x in set1:
    total += x
print(total)

