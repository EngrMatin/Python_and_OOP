n = int(input("Enter a number: "))

original_num = n

reversed_num = 0
while(n>0):
    remainder = n%10
    reversed_num = reversed_num * 10 + remainder
    n = n//10

if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")