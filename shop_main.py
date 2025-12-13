import csv
from datetime import datetime
from product_class import Product
from cart_manager import ShoppingCart

TAX_RATE = 0.18

# Decorator for status
def status(msg):
    def deco(fn):
        def wrap(*a, **k):
            print(f"[STATUS] {msg}...")
            return fn(*a, **k)
        return wrap
    return deco

@status("Loading inventory")
def load_inventory(path="inventory.csv"):
    products = {}
    with open(path, newline="") as f:
        for name, price, stock in csv.reader(f):
            if name == "name":
                continue
            products[name] = Product(name, float(price), int(stock))
    return products

@status("Saving inventory")
def save_inventory(products, path="inventory.csv"):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "price", "stock"])
        for p in products.values():
            w.writerow(p.to_row())

@status("Saving order")
def save_order(cart, path="orders.csv"):
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for product, qty in cart.items.items():
            line_total = product.price * qty
            w.writerow([date, product.name, qty, product.price, line_total])

# --- Demo Flow ---
products = load_inventory()
cart = ShoppingCart()

# Display catalog
print("E-COMMERCE ORDER SYSTEM")
print("Available Products:")
for i, p in enumerate(products.values(), 1):
    print(f"{i}. {p.name} - {int(p.price)} ({p.stock} in stock)")

# Add items (sample)
cart.add(products["Laptop"], 1)
cart.add(products["Mouse"], 2)

# Reduce stock
for product, qty in cart.items.items():
    product.reduce_stock(qty)

# Billing
subtotal = cart.subtotal()
tax = (lambda s: s * TAX_RATE)(subtotal)
total = subtotal + tax

print("\nSHOPPING CART:")
for product, qty in cart.items.items():
    print(f"{product.name} (Qty: {qty}) - {int(product.price * qty)}")

print("\nBILL SUMMARY:")
print(f"Subtotal: {int(subtotal)}")
print(f"Tax (18%): {int(tax)}")

save_order(cart)
save_inventory(products)
print("Order saved to: orders.csv")