def replace_word(lst, str):
    
    textList = list(str.split())
    
    for i in range(len(lst)-1):
        for word in textList:
            if word == lst[i]:
                str = str.replace(word, lst[i+1])
    return str

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]   
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

result = replace_word(replace_with, s)
print(result)
