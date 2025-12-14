import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")

# Sales summary
item_sales = df.groupby("item")["quantity"].sum()

# Revenue calculations
revenue = np.sum(df["line_total"])
aov = revenue / df["order_id"].nunique()

print("Total Revenue:", revenue)
print("Average Order Value:", aov)

# Save numeric analysis to CSV
summary_df = pd.DataFrame({
    "Total Revenue": [revenue],
    "Average Order Value": [aov]
})
summary_df.to_csv("sales_summary.csv", index=False)

print("Total Revenue:", revenue)
print("Average Order Value:", aov)
print("Sales summary saved to sales_summary.csv")

# Plot and SAVE instead of show
plt.figure()
item_sales.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("top_selling_products.png")
plt.close()

print("Graph saved as top_selling_products.png")