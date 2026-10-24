# Function that accepts variable number of items (packing with *args)
def calculate_total(*items):
    print("Items in cart:", items)
    return sum(items)

# Function that accepts variable keyword arguments (packing with **kwargs)
def print_invoice(customer_name, **details):
    print(f"Invoice for {customer_name}")
    for key, value in details.items():
        print(f"{key}: {value}")

# _ Unpacking Example _

# Order items (list of prices)
order_items = [250, 100, 75]   # Prices of products
total_amount = calculate_total(*order_items)   # Unpacking list
print("Total Amount:", total_amount)

# Order details (dictionary)
order_details = {
    "Product": "Laptop",
    "Quantity": 1,
    "Price": total_amount,
    "Payment Method": "Credit Card"
}

# Passing dictionary as keyword args
print_invoice("Farhan", **order_details)