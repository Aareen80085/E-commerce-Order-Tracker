import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")

# Sales summary
item_sales = df.groupby("item")["quantity"].sum().sort_values(ascending=False)

# Revenue metrics
revenue = np.sum(df["line_total"].values)
aov = revenue / df["date"].nunique()

print("Total Revenue:", revenue)
print("Average Order Value:", aov)

# Visualization
item_sales.plot(kind="bar")
plt.title("Top-Selling Items")
plt.xlabel("Item")
plt.ylabel("Units Sold")
plt.show()