print("PROGRAM STARTED")
# Decorator for automation status messages
def status(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[STATUS] {msg}...")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Product:

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


@status("Saving order")
def save_order(cart, path="orders.csv"):
    import os
    import csv
    from datetime import datetime
    import random

    file_exists = os.path.exists(path)
    order_id = f"ORD{random.randint(1000,9999)}"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)

        # Write header if file is new or empty
        if not file_exists or os.stat(path).st_size == 0:
            writer.writerow(["date", "order_id", "item", "quantity", "price", "line_total"])

        for product, qty in cart.items.items():
            line_total = product.price * qty
            writer.writerow([date, order_id, product.name, qty, product.price, line_total])

    print(f"Order saved with Order ID: {order_id}")
    return order_id


if __name__ == "__main__":

    # Sample inventory (temporary, no CSV yet)
    products = {
        "Laptop": Product("Laptop", 50000, 5),
        "Mouse": Product("Mouse", 500, 20),
        "Keyboard": Product("Keyboard", 1500, 15)
    }

    from cart_manager import ShoppingCart

    cart = ShoppingCart()

    print("\nE-COMMERCE ORDER SYSTEM")
    print("Available Products:")
    for i, p in enumerate(products.values(), 1):
        print(f"{i}. {p.name} - {int(p.price)} ({p.stock} in stock)")

    # User input (controlled)
    qty_laptop = int(input("\nEnter quantity for Laptop (default 1): ") or 1)
    cart.add_item(products["Laptop"], qty_laptop)
    products["Laptop"].reduce_stock(qty_laptop)

    qty_mouse = int(input("Enter quantity for Mouse (default 2): ") or 2)
    cart.add_item(products["Mouse"], qty_mouse)
    products["Mouse"].reduce_stock(qty_mouse)

    cart.display_cart()

    # Discount coupon logic (fixed 18% discount)
    discount = 0
    coupon_code = "SAVE18"

    user_coupon = input("\nEnter discount coupon code (or press Enter to skip): ").strip()
    if user_coupon == coupon_code:
        discount = order_discount = (sum(p.price * q for p, q in cart.items.items())) * 0.18
        print("Coupon applied! 18% discount activated.")
    elif user_coupon:
        print("Invalid coupon code. No discount applied.")

    order = Order(cart, discount=discount)

    print("\nBILL SUMMARY:")
    print("Subtotal:", int(order.subtotal()))
    print("Tax (18%):", int(order.tax()))
    print("Total:", int(order.total()))

    order_id = save_order(cart)