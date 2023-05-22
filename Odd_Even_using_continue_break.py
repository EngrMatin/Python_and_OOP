for x in range(20):
    if x%2 == 0:
        continue
    print(x, end=' ')

print("\n")

for x in range(20):
    if x%2 != 0:
        continue
    print(x, end=' ')

print("\n")

i = 12
while i>=0:
    i += 1
    if i%2 == 0:
        continue
    if i >= 40:
        break
    print(i, end=' ')

print("\n")

i = 0
while i>=0:
    i += 1
    if i%2 != 0:
        continue
    if i >= 20:
        break
    print(i, end=' ')

print("\n")



