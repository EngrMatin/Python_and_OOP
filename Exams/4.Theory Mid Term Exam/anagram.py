def isAnagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if isAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are NOT anagram of each other")
