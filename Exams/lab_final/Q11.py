from abc import ABC, abstractmethod

class ProgrammingHero(ABC):                   # Abstract Class for Observable Class
    
    @abstractmethod                           
    def attach(self, observer):               # Abstract method for Observable Class
        pass
    
    @abstractmethod
    def detach(self, observer):               # Abstract method for Observable Class
        pass
    
    @abstractmethod
    def notify(self):                         # Abstract method for Observable Class
        pass


class Phitron(ProgrammingHero):                                   # Observable Class
    
    _observers_list = list()

    def attach(self, observer):
        print(f'{observer.name} has been added to Phitron team!')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'{observer.name} has been removed from Phitron team!')
        self._observers_list.remove(observer)

    def notify(self):
        print('Meeting started!')
        for observer in self._observers_list:
            observer.update()


class Admin(ABC):                             # Abstract Class for Observer Class
    
    @abstractmethod
    def update(self, subject):                # Abstract method for Observer Class
        pass


class ChiefAdvisor(Admin):                                  # Observer Class
    def __init__(self, name):
        self.name = name                                            

    def update(self):
        message = 'Design the Program Outline'
        print(f'{self.name} {message}')

class Advisor(Admin):                                       # Observer Class
    def __init__(self, name):
        self.name = name

    def update(self):
        message = 'Create a Facebook group'
        print(f'{self.name} {message}')

class Moderator(Admin):                                     # Observer Class
    def __init__(self, name):
        self.name = name

    def update(self):
        message = 'Coordinate the admission process'
        print(f'{self.name} {message}')

class GroupExpert(Admin):                                   # Observer Class
    def __init__(self, name):
        self.name = name

    def update(self):
        message = 'Design the Student Leaderboard'
        print(f'{self.name} {message}')

class Expert(Admin):                                        # Observer Class
    def __init__(self, name):
        self.name = name

    def update(self):
        message = 'Formulate the Support Team'
        print(f'{self.name} {message}')

class Faculty(Admin):                                       # Observer Class
    def __init__(self, name):
        self.name = name

    def update(self):
        message = 'Prepare modules for Data Structure'
        print(f'{self.name} {message}')



if __name__ == "__main__":

    publisher = Phitron()

    chiefAdv = ChiefAdvisor('Jhankar Mahbub')
    publisher.attach(chiefAdv)

    adv = Advisor('Emdadul Haque Tareque')
    publisher.attach(adv)

    mod = Moderator('Rahat Khan Pathan')
    publisher.attach(mod)

    grExp = GroupExpert('Shahadat Hossain')
    publisher.attach(grExp)

    exp = Expert('Avishek Devnath')
    publisher.attach(exp)

    fac = Faculty('Akib Zaman')
    publisher.attach(fac)

    publisher.detach(fac)

    publisher.notify()


    '''
    OUTPUT: 
Jhankar Mahbub has been added to Phitron team!
Emdadul Haque Tareque has been added to Phitron team!
Rahat Khan Pathan has been added to Phitron team!
Shahadat Hossain has been added to Phitron team!
Avishek Devnath has been added to Phitron team!
Akib Zaman has been added to Phitron team!
Akib Zaman has been removed from Phitron team!

Akib Zaman: Why do you guys always do this to me!

Meeting started!
Jhankar Mahbub Design the Course Outline
Emdadul Haque Tareque Create a Facebook group
Rahat Khan Pathan Coordinate the admission process
Shahadat Hossain Design the Student Leaderboard
Avishek Devnath Formulate the Support Team

    '''