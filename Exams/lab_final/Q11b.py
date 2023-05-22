class GroupChat:                                      # Observable Class                     
    def __init__(self):
        self.__observers = []

    def subscribe(self, observer):
        self.__observers.append(observer)

    def add_new_event(self, msg):
        self.notify(msg)

    def notify(self, msg):
        for observer in self.__observers:
            observer.update(msg)
    
    def unsubscribe(self, observer):
        self.__observers.remove(observer)


class Subscriber:                                       # Observer Class
    def __init__(self, name):
        self.name = name
    
    def update(self, msg):
        print(f'New Message for {self.name}: {msg}')


if __name__ == "__main__":
    messenger = GroupChat()

    akib = Subscriber('Akib Zaman')
    rakib = Subscriber('Rakib Chowdhury')
    sakib = Subscriber('Sakib Al Hasan')
    yakub = Subscriber('Yakub Shorkar')

    messenger.subscribe(akib)
    messenger.subscribe(rakib)
    messenger.subscribe(sakib)
    messenger.subscribe(yakub)

    messenger.add_new_event('Good morning! How are you? We have a meeting tomorrow at 10 AM.')

    messenger.unsubscribe(yakub)
    
    messenger.add_new_event("Hi brother! Today's meeting has been postponed")