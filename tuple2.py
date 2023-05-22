tuple1 = (1,2,3,4,5)
# tuple1[0] = 6         # error  tuple elements are NOT changeable

tuple2 = (1,2,3,4,[5,6,7])
tuple2[4][0] = 100      # it is a list element
print(tuple2)           # (1, 2, 3, 4, [100, 6, 7])

# tuple2[4] = 200       # error  tuple elements are NOT changeable
