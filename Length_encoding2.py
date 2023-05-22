from collections import OrderedDict

def runLengthEncoding(input):
 
    dict=OrderedDict.fromkeys(input, 0)    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
 
    for ch in input:
        dict[ch] += 1                # dict = {'w':4,'a':3,'d':1,'e':1,'x':6}
 
    output = ''
    for key,value in dict.items():
        output = output + key + str(value)
    return output
 
 
if __name__ == "__main__":
    input="wwwwaaadexxxxxx"
    print (runLengthEncoding(input))