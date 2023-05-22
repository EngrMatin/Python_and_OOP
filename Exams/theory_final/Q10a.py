class Parent:
    def __init__(self):
        self.name = 'Parent Chowdhury'
        self.district = 'Cumilla'

class Child(Parent):
    def __init__(self):
        self.name = 'Child Chowdhury'
        super().__init__()


kid = Child()
print(kid.district)