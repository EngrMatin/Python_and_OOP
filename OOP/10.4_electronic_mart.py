class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        print('running the laptop')

    def purchase(self, money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price

class Phone:
    def __init__(self, brand, price, color, camera, sim_num):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num

    def is_dual_sim(self):
        return self.sim_num > 1

class Watch:
    def __init__(self, brand, price, color, watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital(self):
        return self.watch_type == 'digital'


class Manager:
    def __init__(self, name, designation, salary, experience) -> None:
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
    def __init__(self, name, designation, salary, commission) -> None:
        self.name = name
        self.designation = designation
        self.salary = salary
        self.commission = commission

    def handle_customer(self):
        pass
 
    def withdraw_salary(self):
        pass












