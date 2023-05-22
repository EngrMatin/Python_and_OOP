# inheritance
# DRY --> Do not Repeat Yourself
# base class will have only the common attributes and methods

class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def re_sale(self):
        print('ready to sell again')

class Laptop(Device):
    def __init__(self, brand, price, color, memory):
        super().__init__(brand, price, color)
        self.memory = memory

    def run(self):
        print('running the laptop')

    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price

    def __repr__(self) -> str:
        return f'Laptop {self.brand} : {self.price} : {self.color}'

class Phone(Device):
    def __init__(self, brand, price, color, camera, sim_num):
        super().__init__(brand, price, color)
        self.camera = camera
        self.sim_num = sim_num

    def is_dual_sim(self):
        return self.sim_num > 1

    def __repr__(self) -> str:
        return f'Phone {self.brand} : {self.price} : {self.color}'

class Watch(Device):
    def __init__(self, brand, price, color, watch_type) -> None:
        super().__init__(brand, price, color)
        self.watch_type = watch_type

    def is_digital(self):
        return self.watch_type == 'digital'

    def __repr__(self) -> str:
        return f'Watch {self.brand} : {self.price} : {self.color}'


class Manager:
    def __init__(self, name, designation, salary, experience):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.experience = experience

    def day_total_sales(self):
        pass

    def handle_customer_complain(self):
        pass

    def withdraw_salary(self):
        pass

class SalesPerson:
    def __init__(self, name, designation, salary, commission):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.commission = commission

    def handle_customer(self):
        pass
 
    def withdraw_salary(self):
        pass

lenovo = Laptop('Lenovo', 50000, 'Black', '8 GB')
hp = Laptop('HP', 45000, 'Silver', '6 GB')
print(lenovo)
print(hp)

oppo = Phone('Oppo', 15000, 'Black', '15MP', 2)
samsung = Phone('Samsung', 26000, 'Silver', '24MP', 1)
print(oppo)
print(samsung)

hp.re_sale()
print(hp.brand)