class Calculator:

    def __init__(self, x, n):
        self.x = x
        self.n = n

    def sum(self):
        return self.x + self.n

    def pow(self):
        return self.x ** self.n

myCalc = Calculator(5, 3)
summation = myCalc.sum()
exp = myCalc.pow()

print(f'Summation: {summation}, Exponentiation: {exp}')
