def isPalindrome(str):
    if str == str[ : :-1]:
        return True
    return False

str = input('Enter a string: ')

if isPalindrome(str):
    print('Palindrome')
else:
    print('Not palindrome')