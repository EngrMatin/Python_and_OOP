class GrandParent:
    def __init__(self):
        self.name = 'GrandParent Chowdhury'
        self.country = 'Bangladesh'

class Parent(GrandParent):
    def __init__(self):
        self.name = 'Parent Chowdhury'
        self.district = 'Cumilla'
        super().__init__()

class Child(Parent):
    def __init__(self):
        self.name = 'Child Chowdhury'
        super().__init__()


kid = Child()
print(kid.district)
print(kid.country)