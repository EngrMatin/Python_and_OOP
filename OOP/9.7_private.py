class User:
    def __init__(self, name, password, phone) -> None:
        self.name = name
        self.__password = password
        self.__phone = phone

    def __get_password(self):
        print(self.__password)

    def user_login(self, name, password):
        if(name == self.name and password == self.__password):
            return True
        return False

ryan = User('Ryan Dhali', 'ABCDE', '01715529212')
# print(ryan.__password) # error
# print(ryan.__phone)   # error
# ryan.get_password()
result = ryan.user_login('Ryan Dhali', 'ABCDE')
print(result)
