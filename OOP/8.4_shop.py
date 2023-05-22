class Shop:
    cart = []               # class attribute (static)

    def __init__(self, buyer):
        self.buyer = buyer           # instance attributes

    def add_to_cart(self, item):
        self.cart.append(item)

shopper1 = Shop('Alu Khan')
shopper1.add_to_cart('T-shirt')
print(shopper1.cart)

shopper2 = Shop('Potol Khan')
shopper2.add_to_cart('shoes')
print(shopper2.cart)
    