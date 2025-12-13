class product:

#this represents all the products in the store

    def __init__(self,product_id, name, price, stock ):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

#This Method updates quantity attribute from the product class
    def update_stock(self, quantity):
        self.stock += quantity

#This method checks whether the product is available in the requested quantity
    def is_available(self,quantity =1 ):
        return self.quantity >= quantity #returns boolean if enough stock or not

def __str__(self):
        return f"{self.name} - {self.price:,.0f} ({self.stock} in stock)"
    
def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, stock={self.stock})"

class Order:

#Represents a customer order
    
    def __init__(self, order_id, items, discount_code=None):
        self.order_id = order_id
        self.items = items  # List of tuples: (Product, quantity)
        self.discount_code = discount_code
        self.tax_rate = 0.18  # 18% tax
        self.discount_rate = 0.0
        
        # Apply discount codes
        if discount_code == "SAVE10":
            self.discount_rate = 0.10
        elif discount_code == "SAVE20":
            self.discount_rate = 0.20

#Total price of all items 
def calculate_subtotal(self):
    line_totals = []
    subtotal= list(map(lambda product, quantity: product*quantity,line_totals))
    return sum(subtotal)


#Calculates how much money to subtract based on discount code
def calculate_discount(self):
        """Calculate discount amount"""
        return self.calculate_subtotal() * self.discount_rate

#Calculate tax using lambda
def calculate_tax(self):
        subtotal_after_discount = self.calculate_subtotal() - self.calculate_discount()
        return subtotal_after_discount * self.tax_rate


# Calculate final total
def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return subtotal - discount + tax

#Final order summary
def get_order_summary(self):
        """Return formatted order summary"""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        total = self.calculate_total()

        # Lambda functions for efficient formatting
        format_currency = lambda amount: f"₹{amount:,.2f}"
        format_line = lambda label, amount: f"{label}: {format_currency(amount)}\n"
        
        # Build summary lines using lambda-based approach
        summary_lines = [
            "\n" + "="*50 + "\n",
            "BILL SUMMARY:\n",
            "="*50 + "\n",
            format_line("Subtotal", subtotal)
        ]
        
        # Add discount section if applicable using conditional lambda
        if discount > 0:
            discount_section = [
                f"Discount ({self.discount_code}): -{format_currency(discount)}\n",
                f"After Discount: {format_currency(subtotal - discount)}\n"
            ]
            summary_lines.extend(discount_section)
        
        # Add tax and total using lambda formatting
        summary_lines.extend([
            format_line("Tax (18%)", tax),
            "-"*50 + "\n",
            format_line("Total", total),
            "="*50 + "\n"
        ])
        
        # Join all lines efficiently
        summary = "".join(summary_lines)
        return summary
