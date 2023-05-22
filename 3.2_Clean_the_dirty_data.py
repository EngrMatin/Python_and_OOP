data = input("Enter uncleaned data: ")
new_data = data.lower()

ans = ''
for i in new_data:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        # print(f"{i} found")
        ans += i + ' '

print(ans)