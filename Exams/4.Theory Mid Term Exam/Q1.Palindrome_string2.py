def isPalindrome(str):
    revStr = ''.join(reversed(str))
    if str == revStr:
        return True
    return False

str = input('Enter a string: ')

if isPalindrome(str):
    print('Palindrome')
else:
    print('Not palindrome')