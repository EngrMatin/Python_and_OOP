class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name
        self.email = f'{self.first}.{self.last}@user.com'

    def get_email(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, value):
        self.first = value.split(' ')[0]
        self.last = value.split(' ')[1]

person = User('mark', 'zuku')
print(person.first)  
print(person.email)   
print('\n')
print(person.get_email())
print('\n')
# print(person.full_name())
print('\n')
print(person.full_name)  # using @property    # here, full_name is a property, not method
print('\n')

person.full_name = 'Tom Hanks' # using @full_name.setter
print(person.full_name)
