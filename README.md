Case Study: E-commerce Order Tracker with CSV Storage

⸻

1. Introduction to the Case Study

This case study focuses on the development of a console-based E-commerce Order Tracker using Python. The system replicates the core functionality of an online shopping platform, allowing users to manage products, add items to a cart, place orders, and analyze sales data. The project emphasizes modular design, object-oriented programming, file handling, and data analysis techniques.

⸻

2. Problem Statement / Case Background (Abstract)

The rapid growth of e-commerce platforms requires efficient mechanisms to manage orders, inventory, and sales analytics. This project addresses the need for a lightweight, non-database-driven order tracking system that can store transaction data persistently and generate meaningful analytical insights. The system is implemented using Python and CSV files to maintain simplicity and transparency.

⸻

3. Problem Statement / Case Study Design

The system is designed using a modular architecture, where each module handles a specific responsibility:
	•	shop_main.py – User interface and application control
	•	product_class.py – Product and order logic
	•	cart_manager.py – Shopping cart operations
	•	analytics.py – Sales analysis and visualization

CSV files (inventory.csv and orders.csv) are used for persistent storage. The design ensures separation of concerns, maintainability, and ease of debugging.

⸻

4. Methods & Algorithms Technology Applied in the Case Study

Technologies Used
	•	Python 3
	•	CSV file handling
	•	Pandas for data analysis
	•	NumPy for numerical computation
	•	Matplotlib for data visualization

Methods & Algorithms
	•	Dictionary-based data structures for cart management
	•	Iterative aggregation algorithms for subtotal and billing
	•	Decorator pattern for automation and status display
	•	Lambda expressions for concise tax and total calculations
	•	GroupBy aggregation using Pandas for item-wise sales analysis

⸻

5. Problem Statement / Case Study Implementation Details and Snapshots

Project Structure
E-commerce Order Tracker/
├── shop_main.py
├── product_class.py
├── cart_manager.py
├── analytics.py
├── inventory.csv
├── orders.csv

Implementation Highlights
	•	Menu-driven console interface
	•	Coupon-based discount system (fixed 18%)
	•	Dynamic inventory updates after order placement
	•	CSV-based persistence for orders and products
	•	On-demand execution of sales analytics
	•	Safe handling of malformed or empty CSV files



