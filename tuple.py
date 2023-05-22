list1 = [11, 22, 33, 22, 33, 11, 44, 55, 22, 11]
print(list1)

tuple1 = tuple(list1)
print(tuple1)             # Items cannot be added, removed or changed in tuple

tuple2 = (1, 2, 3, 2, 3, 4, 2, 4, 5)
print(tuple2)
                                     # x = 10   here x is a regular variable
                                     # x = 10,  here x will be a tuple
tuple3 = 10, 20, 30, 40, 50, 60, 70    
print(tuple3)
print(tuple3[2])   # to copy: alt+shift+downArrow
print(tuple3[-7])
print(tuple3[1:4])  # list[start, end(exclusive), step]
print(tuple3[ :4]) 
print(tuple3[4: ]) 
print(tuple3[ : ]) 
print(tuple3[ : :-1]) 
print(tuple3[ : :2]) 
print(tuple3[ : :-2]) 
print(tuple3[7:2:-1]) 
print(tuple3[-2:-7:-1])

NoOfItems = len(tuple3)
print("No of Items: ", NoOfItems)

print("Sum of the list: ", sum(tuple3))

total = 0
for x in tuple3:
    total += x
print(total)

