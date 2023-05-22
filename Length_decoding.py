class Solution:
   def solve(self, str):
      output = ""
      num = ""
      for i in str:
        if i.isalpha():
            output += i*int(num)
            num=""
        else:
            num += i
      return output
obj = Solution() 
print(obj.solve("4B3A2D1C2B"))