import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_analysis():
    # Check if file exists and is non-empty
    if not os.path.exists("orders.csv") or os.stat("orders.csv").st_size == 0:
        print("orders.csv is missing or empty. No data to analyze.")
        return

    # Read CSV with error handling for inconsistent rows
    try:
        df = pd.read_csv("orders.csv", on_bad_lines='skip')  # skip malformed lines
    except pd.errors.ParserError as e:
        print(f"Error reading orders.csv: {e}")
        return

    required_cols = {"order_id", "item", "quantity", "line_total"}
    if not required_cols.issubset(df.columns):
        print("orders.csv has invalid format. Cannot perform analysis.")
        return

    # Sales summary
    item_sales = df.groupby("item")["quantity"].sum()

    # Revenue calculations
    revenue = np.sum(df["line_total"])
    aov = revenue / df["order_id"].nunique()

    print("\n--- SALES ANALYTICS ---")
    print("Total Revenue:", int(revenue))
    print("Average Order Value:", int(aov))

    # Save numeric analysis to CSV
    summary_df = pd.DataFrame({
        "Total Revenue": [revenue],
        "Average Order Value": [aov]
    })
    summary_df.to_csv("sales_summary.csv", index=False)
    print("Sales summary saved to sales_summary.csv")

    # Plot and save graph
    plt.figure()
    item_sales.plot(kind="bar")
    plt.title("Top Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig("top_selling_products.png")
    plt.close()
    print("Graph saved as top_selling_products.png")

if __name__ == "__main__":
    run_analysis()