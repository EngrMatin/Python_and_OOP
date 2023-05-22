str = input("Enter a string: ")
new_str = ''
for i in range(len(str)):
    if str[i].islower():
        new_str += str[i].upper()
    elif str[i].isupper():
        new_str += str[i].lower()
    else:
        new_str += str[i]

print(new_str)

print(str.swapcase())    # equivalent function