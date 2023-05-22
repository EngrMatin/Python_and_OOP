class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license
        self.price = price
        print('Vehicle class init is called')

    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self, name, license, price, seats, ticket_price):
        self.seats = seats
        self.available_seats = seats
        self.ticket_price = ticket_price
        print('Bus class init is called')
        super().__init__(name, license, price)
        
    def sell_ticket(self, customer_name, quantity, amount):
        self.available_seats -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)
        return 'No ticket for you'

class AC_Bus(Bus):
    def __init__(self):
        print('AC bus created')

class Mini_Bus(Bus):
    def __init__(self):
        print('Mini bus created')
        super().__init__('Mimi mini', 'GHA9759', 2000000, 20, 500)

class Ticket:
    def __init__(self, owner) -> None:
        self.owner = owner

mini = Mini_Bus()
print(mini.name)

            