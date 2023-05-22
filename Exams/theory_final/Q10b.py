class GrandParent:
    def __init__(self):
        self.name = 'GrandParent Chowdhury'
        self.country = 'Bangladesh'

class Parent:
    def __init__(self):
        self.name = 'Parent Chowdhury'
        self.district = 'Cumilla'

class Child(Parent, GrandParent):
    def __init__(self):
        self.name = 'Child Chowdhury'
        GrandParent.__init__(self)
        Parent.__init__(self)


kid = Child()
print(kid.district)
print(kid.country)