def nearly_equal(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    count = 0
    i = j = 0
    while(i<l1 and j<l2):
        if(str1[i] != str2[j]):
            count += 1

            if(l1>l2):
                i += 1
            elif(l1<l2):
                i -= 1
        
        if(count>1):
            return False
        i += 1
        j += 1

    if(count<2):
            return True
  

str1 = input("Enter first string::\n")
str2 = input("Enter second string::\n")

ans = nearly_equal(str1, str2)
if(ans):
    print("Strings are nearly equal.")
else:
    print("Strings are NOT equal.")