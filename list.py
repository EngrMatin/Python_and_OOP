list1 = [00, 11, 22, 33, 44, 55, 66, 77, 88]

print(list1[2])   # to copy: alt+shift+downArrow
print(list1[-7])
print(list1[1:5])  # list[start, end(exclusive), step]
print(list1[ :5]) 
print(list1[5: ]) 
print(list1[ : ]) 
print(list1)               # select and press F2 to replace a word in all place
print(list1[ : :-1]) 
print(list1[ : :2]) 
print(list1[ : :-2]) 
print(list1[7:2:-1]) 
print(list1[-2:-7:-1]) 

list1.append(90)
print(list1)

list1.insert(1, 10)
print(list1)

list1.remove(10)
print(list1)

list1.pop()
print(list1)

poppedItem = list1.pop(2)
print("Popped Item: ", poppedItem)
print(list1)

NoOfItems = len(list1)
print("No of Items: ", NoOfItems)

key = 55
NoOfOccurrence = list1.count(key)
print(f"No of Occurrence of {key}: {NoOfOccurrence}")

list1.reverse()
print(list1)

list1.sort()
print(list1)

print("Sum of the list: ", sum(list1))

total = 0
for x in list1:
    total += x
print(total)

list1.clear()   
print(list1)




