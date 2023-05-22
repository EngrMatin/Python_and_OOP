class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 1000000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'No money for you. Minimum withdraw: {self.min_withdraw}'
        elif amount > self.max_withdraw:
             return f'you crossed max limit: {self.max_withdraw}'
        elif amount > self.balance:
            return 'You are broke!!! No money for you'
        else:
            self.balance = self.balance - amount
            return f'Here is your money: {amount}'

    def deposit(self, amount):
        self.balance = self.balance + amount
        
my_bank = Bank(20000)

reply = my_bank.withdraw(100)
print(reply)

reply = my_bank.withdraw(50000)
print(reply)

reply = my_bank.withdraw(5000)
print(reply)
print(my_bank.get_balance())

my_bank.deposit(12000)
print(my_bank.get_balance())
