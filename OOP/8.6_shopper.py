class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        print(self.cart)
        price = 0
        for item in self.cart:
            #print(item)
            price += item['price'] * item['quantity']
        print(price)

        if amount < price:
            return f'Please give me more money: {price - amount}'
        elif amount > price:
            return f'Here is the change: {amount - price}'
        else:
            return 'Thanks a lot'

shopping = Shopper('Sakib Khan')
shopping.add_to_cart('shirt', 1000, 3)
shopping.add_to_cart('pant', 1200, 3)
shopping.add_to_cart('shoes', 3000, 2)

reply = shopping.checkout(9000)
print(reply)

reply = shopping.checkout(15000)
print(reply)

