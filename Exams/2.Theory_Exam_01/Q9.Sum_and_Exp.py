class Calculator:

    def sum(self, x, n):
        return x+n

    def pow(self, x, n):
        return x**n

myCalc = Calculator()
summation = myCalc.sum(5,3)
exp = myCalc.pow(5,3)

print(summation)
print(exp)