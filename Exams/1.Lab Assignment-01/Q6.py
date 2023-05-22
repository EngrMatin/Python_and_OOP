def clean_string(text):
    
    output = ""
    for x in text:
        if x>='a' and x<='z' or x>='A' and x<='Z':
            output += x
    
    return output


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)