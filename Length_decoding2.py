class Decoding:
   def decode(self, str):
      output = ""
      ch = ''
      for i in str:
        if i.isalpha()==False:
            output += ch*int(i)
        else:
            ch = i
      return output

obj = Decoding() 
ans = obj.decode("x3b4U5i2")
# print(ans)
result = "".join(sorted(ans, key = lambda x:x.lower()))
print(result)
