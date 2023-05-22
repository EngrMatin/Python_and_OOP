class Bus:
    owner = "Ena Transport"

    def __init__(self, route, license, driver):
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []  

    def start_trip(self, start_time):
        self.trip.append(start_time)
    
class Driver:
    def __init__(self, name, license, mobile, address, salary):
        pass

    def drive(self, start, end):
        pass

    def take_vacation(self):
        pass

    def withdraw_salary(self):
        pass

class Passanger:
    def __init__(self, name, mobile, destination):
        self.name = name
        self.mobile = mobile
        self.destination = destination

    def purchase_ticket(self, destination, money):
        pass

class Manager:
    def __init__(self, name, mobile, department):
        pass

class Counter:
    def __init__(self, manager, location):
        pass

num = 55
name = 'Ena'
passenger1 = Passanger('Rashed', '01718756554', 'Khulna')

print(passenger1)