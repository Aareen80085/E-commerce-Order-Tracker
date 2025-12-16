from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, qty):
        if product in self.items:
            self.items[product] += qty
        else:
            self.items[product] = qty

    def add(self, product, qty):
        self.add_item(product, qty)

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, qty):
        if qty <= 0:
            self.remove_item(product)
        else:
            self.items[product] = qty

    def subtotal(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def is_empty(self):
        return len(self.items) == 0

    def display_cart(self):
        if self.is_empty():
            print("Cart is empty")
            return
        print("\nSHOPPING CART:")
        for product, qty in self.items.items():
            print(f"{product.name} (Qty: {qty}) - {int(product.price * qty)}")