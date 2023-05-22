def create_new_string(lst, string):
    
    lst2 = list(map(lambda x: x.lower(), lst))

    str = ""
    for x in string:
        if x>='a' and x<='z' or x>='A' and x<='Z' or x==' ':
            str += x

    textList = list(str.split())
    newList = list(map(lambda x: x.lower(), textList))
    
    output = ""
    for i in range(len(newList)):
        if newList[i] in lst2:
            output += textList[i+1] + ' '

    return output


a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

result = create_new_string(a, s)

file1 = open("out.txt","w")
file1.write(result)
file1.close()