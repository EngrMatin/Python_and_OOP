class Phone:

    manufactured = 'china'       # class attribute (static)

    def __init__(self, brand, color, price):
        self.brand = brand         # instance attributes
        self.color = color
        self.price = price

    def send_sms(self, number, text):
        sms = f"sending sms: {text} to {number}"
        return sms

my_phone = Phone('Oppo', 'blue', 17000)
print(my_phone.brand, my_phone.manufactured)

her_phone = Phone('iPhone', 'purple', 95000)
print(her_phone.brand, her_phone.color)

mom_phone = Phone('Nokia', 'black', 2500)
print(my_phone.price, her_phone.price, mom_phone.price)
