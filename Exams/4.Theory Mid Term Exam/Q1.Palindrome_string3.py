str = input('Enter a string: ')
newStr = ''
for i in str:
    newStr = i + newStr

if str == newStr:
    print('Palindrome')
else:
    print('Not palindrome')