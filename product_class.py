class product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, qty):
        if qty > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= qty

    def to_row(self):
        return [self.name, self.price, self.stock]
    
class Order:
    def __init__(self, cart, tax_rate=0.18, discount=0):
        self.cart = cart
        self.tax_rate = tax_rate
        self.discount = discount

    def subtotal(self):
        return sum(p.price * q for p, q in self.cart.items.items())

    def tax(self):
        return self.subtotal() * self.tax_rate

    def total(self):
        return self.subtotal() + self.tax() - self.discount