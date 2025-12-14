from collections import defaultdict

class shoppingcart:
    def __init__(self):
        self.items = defaultdict(int)  # product -> qty

    def add(self, product, qty):
        self.items[product] += qty

    def update(self, product, qty):
        if qty <= 0:
            self.items.pop(product, None)
        else:
            self.items[product] = qty

    def remove(self, product):
        self.items.pop(product, None)

    def subtotal(self):
        return sum(map(lambda p: p[0].price * p[1], self.items.items()))

    def is_empty(self):
        return len(self.items) == 0