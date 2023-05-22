data = input("Enter data: ")
shift = 1

ans = ''

for character in data:
    ans += chr((ord(character)+shift-97)%26 +97)

print(ans)
