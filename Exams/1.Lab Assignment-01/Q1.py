def create_string(list):
    str1 = ""
    for x in list:
        str1 += x+' '
    return str1

l = ["This", "is", "very", "fantastic"]
print(create_string(l))

# Technique-2:
def create_string(list):
    str1 = " "
    return (str1.join(list))

l = ["This", "is", "very", "fantastic"]
print(create_string(l))

# Technique-3:
l = ["This", "is", "very", "fantastic"]
createString = ' '.join([str(x) for x in l])
print(createString)

# Technique-4:
l = ["This", "is", "very", "fantastic"]
listToString = ' '.join(map(str, l))
print(listToString)

# Technique-5:
l = ["This", "is", "very", "fantastic"]
listToStr = ' '.join([str(x) for i, x in enumerate(l)])
print(listToStr)

# Technique-6:
l = ["This", "is", "very", "fantastic"]
for x in l:
    print(x, end=" ")
