from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    @abstractmethod   
    def eat(self):    # Any child class must have this method
        pass
    
    @property
    @abstractmethod
    def name(self):         # Any child class must have this method --> property
        pass
    
    @abstractmethod
    def move(self):             # Any child class must have this method
        print('moving around in the zoo')

class Monkey(Animal):
    def __init__(self):
        self.__name = 'monkey'
    def sing(self):
        print('monkey is signing')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self):
        print('eating banana')
    
    def move(self):
        print('hanging on the branches of the trees')
        super().move()


class Tiger(Animal):
    def eat(self):
        pass
    def move(self):
        pass

layka = Monkey()
print(layka)
layka.eat()
layka.move()
layka.name = 'moonkey'
print(layka.name)