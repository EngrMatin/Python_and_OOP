def reverseWord(string):
 
    wordList = string.split()
     
    newList = [word[::-1] for word in wordList]
     
    newString = " ".join(newList)
 
    return newString
 

result = input("Enter a sentence: ")

print(reverseWord(result))