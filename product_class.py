class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, qty):
        if qty < 0:
            raise ValueError("Invalid stock")
        self.stock = qty

    def reduce_stock(self, qty):
        if qty > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= qty

    def to_row(self):
        return [self.name, self.price, self.stock]