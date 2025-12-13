import csv
import os
import datetime
from product_class import product, Order



class shoppingcart:
#manages shopping cart
    def __init__(self):
        self.item={
            1: (laptop_object, 2),
            2: (mouse_object, 1)
        }

    def add_item(self,product, quantity=1):
        if not product.is_available(quantity):
            print(f"❌ Sorry, only {product.stock} units available for {product.name}")
            return False
    
        if product.product_id in self.items:
            current_qty = self.items[product.product_id][1]
            new_qty = current_qty + quantity
        
            if product.is_available(new_qty):
                self.items[product.product_id] = (product, new_qty)
                print(f"Updated {product.name} quantity to {new_qty}")
            else:
                print(f"Cannot add {quantity} more. Only {product.stock} units available.")
                return False
        else:
            self.items[product.product_id] = (product, quantity)
            print(f"Added {quantity}x {product.name} to cart")
    
        return True

    def remove_item(self,product_id):
        if product_id in self.items:
            product_name = self.items[product_id][0].name
            del self.items[product_id]
            print(f"Removed {product_name} from cart")
            return True
        else:
            print(f"Item not found in cart")
            return False
    
    def update_quantity(self, product_id, quantity):
        
        pass
    def view_cart(self):
        pass
    def get_items_list(self):
        pass
    def clear_cart(self):
        pass
    def is_empty(self):
        pass
