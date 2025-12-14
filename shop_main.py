import csv
from datetime import datetime
from product_class import product
from cart_manager import shoppingcart

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
    products = {Laptop}
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

# --- Menu Driven App ---
products = load_inventory()
cart = shoppingcart()

while True:
    print("===== E-COMMERCE ORDER SYSTEM =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Products:")
        for i, p in enumerate(products.values(), 1):
            print(f"{i}. {p.name} - {int(p.price)} ({p.stock} in stock)")

    elif choice == "2":
        name = input("Enter product name: ")
        if name not in products:
            print("Product not found")
            continue
        qty = int(input("Enter quantity: "))
        try:
            products[name].reduce_stock(qty)
            cart.add(products[name], qty)
            print("Item added to cart")
        except ValueError as e:
            print(e)

    elif choice == "3":
        if cart.is_empty():
            print("Cart is empty")
        else:
            print("SHOPPING CART:")
            for product, qty in cart.items.items():
                print(f"{product.name} (Qty: {qty}) - {int(product.price * qty)}")

    elif choice == "4":
        if cart.is_empty():
            print("Cart is empty")
            continue
        subtotal = cart.subtotal()
        tax = subtotal * TAX_RATE
        total = subtotal + tax

        print("BILL SUMMARY:")
        print(f"Subtotal: {int(subtotal)}")
        print(f"Tax (18%): {int(tax)}")
        print(f"Total: {int(total)}")

        save_order(cart)
        save_inventory(products)
        print("Order saved to: orders.csv")
        break

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice")