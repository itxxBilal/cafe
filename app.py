from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime

app = Flask(__name__)

class BakerySystem:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            self.orders = pd.read_excel("bakery_orders.xlsx")
        except FileNotFoundError:
            self.orders = pd.DataFrame(columns=["Order_ID", "Customer_Name", "Item", "Quantity", "Order_Date"])

    def save_data(self):
        self.orders.to_excel("bakery_orders.xlsx", index=False)
        print("Data saved successfully.")

    def add_order(self, customer_name, item, quantity):
        order_id = len(self.orders) + 1
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_order = pd.DataFrame([[order_id, customer_name, item, quantity, order_date]],
                                 columns=["Order_ID", "Customer_Name", "Item", "Quantity", "Order_Date"])
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        print("Order added successfully!")

    def view_orders(self):
        if self.orders.empty:
            return "No orders available."
        else:
            return self.orders.to_html(index=False)

    def update_order(self, order_id, new_item, new_quantity):
        if order_id < 1 or order_id > len(self.orders):
            return "Invalid order ID. Order not found."
        else:
            self.orders.at[order_id - 1, "Item"] = new_item
            self.orders.at[order_id - 1, "Quantity"] = new_quantity
            return "Order updated successfully!"

bakery_system = BakerySystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_order', methods=['POST'])
def add_order():
    customer_name = request.form['customer_name']
    item = request.form['item']
    quantity = int(request.form['quantity'])
    bakery_system.add_order(customer_name, item, quantity)
    return redirect('/')

@app.route('/view_orders')
def view_orders():
    orders_html = bakery_system.view_orders()
    return render_template('view_orders.html', orders_html=orders_html)

@app.route('/update_order', methods=['POST'])
def update_order():
    order_id = int(request.form['order_id'])
    new_item = request.form['new_item']
    new_quantity = int(request.form['new_quantity'])
    result = bakery_system.update_order(order_id, new_item, new_quantity)
    return result

class BakerySystem:
    # ... (previous methods)

    def add_order(self, customer_name, item, quantity, price):
        order_id = len(self.orders) + 1
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_order = pd.DataFrame([[order_id, customer_name, item, quantity, price, order_date]],
                                 columns=["Order_ID", "Customer_Name", "Item", "Quantity", "Price", "Order_Date"])
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        print("Order added successfully!")

# ... (previous code)

if __name__ == '__main__':
    app.run(debug=True)

    # ... (previous imports)

class BakerySystem:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            self.orders = pd.read_excel("bakery_orders.xlsx")
        except FileNotFoundError:
            self.orders = pd.DataFrame(columns=["Order_ID", "Customer_Name", "Item", "Quantity", "Price", "Order_Date"])

    def save_data(self):
        self.orders.to_excel("bakery_orders.xlsx", index=False)
        print("Data saved successfully.")

    def add_order(self, customer_name, item, quantity, price):
        order_id = len(self.orders) + 1
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_order = pd.DataFrame([[order_id, customer_name, item, quantity, price, order_date]],
                                 columns=["Order_ID", "Customer_Name", "Item", "Quantity", "Price", "Order_Date"])
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        self.save_data()  # Save the data after adding an order
        print("Order added successfully!")

    def view_orders(self):
        if self.orders.empty:
            return "No orders available."
        else:
            return self.orders.to_html(index=False)

    def update_order(self, order_id, new_item, new_quantity, new_price):
        if order_id < 1 or order_id > len(self.orders):
            return "Invalid order ID. Order not found."
        else:
            self.orders.at[order_id - 1, "Item"] = new_item
            self.orders.at[order_id - 1, "Quantity"] = new_quantity
            self.orders.at[order_id - 1, "Price"] = new_price
            self.save_data()  # Save the data after updating an order
            return "Order updated successfully!"

