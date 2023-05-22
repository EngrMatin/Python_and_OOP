class Person:
    def __init__(self, name, age, height, fund):
        self.name = name
        self.age = age
        self.height = height
        self.fund = fund

    def __add__(self, other):
        return self.fund + other.fund

    def __call__(self):
        return f'This is {self.name} with age {self.age} and have ${self.fund}'

    def __len__(self):
        return self.height

alim = Person('alim', 15, 65, 5000)
dalim = Person('dalim', 15, 66, 7000)

print(alim + dalim)  # addition by using dunder method __add__()

print(alim())        # call by using dunder method __call__()

print(len(alim))   
