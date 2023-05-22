str = input("Enter a string: ")

lower_count = 0
upper_count = 0
digit_count = 0
sp_char_count = 0
for i in range(len(str)):
    if str[i].islower():
        lower_count += 1
    elif str[i].isupper():
        upper_count += 1
    elif str[i].isnumeric():
        digit_count += 1
    else:
        sp_char_count += 1

print("Upper case: ", upper_count, "\nLower case: ", lower_count, "\nDigits: ", digit_count, "\nSpecial Character: ", sp_char_count )

print(f"Upper case:  {upper_count}, Lower case: {lower_count}, Digits: {digit_count}, Special Character: {sp_char_count}")