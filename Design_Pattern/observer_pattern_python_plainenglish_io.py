from abc import ABC, abstractmethod

class AvengersTeam(ABC):
    """
    Interface AvengersTeam represents publisher
    """

    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass


class ConcreteAvengersTeam(AvengersTeam):
    """
    ConcreteAvengersTeam implements interface AvengersTeam
    """

    _observers_list = list()

    def attach(self, observer):
        print(f'{observer.name} added to Avengers team!')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'{observer.name} removed from Avengers team!')
        self._observers_list.remove(observer)

    def notify(self):
        print('Avengers assemble!')
        for observer in self._observers_list:
            observer.update()

class Observer(ABC):
    """
    Interface Observer represnts subscribers
    """

    @abstractmethod
    def update(self, subject):
        pass

class IronMan(Observer):
    name = "Iron Man"

    def update(self):
        print('Iron Man report now')

class CaptainAmerica(Observer):
    name = "Captain America"

    def update(self):
        print('Captain America report now')

class Thor(Observer):
    name = "Thor"

    def update(self):
        print('Thor report now')

class BlackWidow(Observer):
    name = "Black Widow"

    def update(self):
        print('Black Widow report now')

class Hulk(Observer):
    name = "Hulk"

    def update(self):
        print('Hulk report now')

class SpiderMan(Observer):
    name = "Spider Man"

    def update(self):
        print('Spider Man report now')



if __name__ == "__main__":

    publisher = ConcreteAvengersTeam()

    iron_man = IronMan()
    publisher.attach(iron_man)

    captain_america = CaptainAmerica()
    publisher.attach(captain_america)

    thor = Thor()
    publisher.attach(thor)

    black_widow = BlackWidow()
    publisher.attach(black_widow)

    hulk = Hulk()
    publisher.attach(hulk)

    spider_man = SpiderMan()
    publisher.attach(spider_man)

    publisher.detach(spider_man)

    print('\nSpider Man: Why do you guys always do this to me!\n')

    publisher.notify()


    '''
    OUTPUT: 
Iron Man added to Avengers team!
Captain America added to Avengers team!
Thor added to Avengers team!
Black Widow added to Avengers team!
Hulk added to Avengers team!
Spider Man added to Avengers team!
Spider Man removed from Avengers team!

Spider Man: Why do you guys always do this to me!

Avengers assemble!
Iron Man report now
Captain America report now
Thor report now
Black Widow report now
Hulk report now

    '''