# ==========================================================
# 1. DATA STRUCTURES
# ==========================================================

# Dictionary:
products = {
    "P101": {
        "name": "Notebook",
        "price": 250,
        "quantity": 20,
        "category": "Stationery"
    },

    "P102": {
        "name": "Pen",
        "price": 50,
        "quantity": 30,
        "category": "Stationery"
    },

    "P103": {
        "name": "Pencil",
        "price": 20,
        "quantity": 3,
        "category": "Stationery"
    }
}

# List: 
sales = []

# Tuple: 
categories = ("Stationery", "Electronics", "Grocery")

# Set: 
unique_categories = set(categories)


# 2. Helper Functions

def format_money(amount):
    """Format amounts in Pakistani Rupees."""
    return f"Rs. {amount:,.2f}"


# Recursive function
def count_total_items(records, index=0):

    # Base condition
    if index >= len(records):
        return 0

    # Recursive condition
    return records[index]["quantity"] + count_total_items(records, index + 1)


# 3. ADD PRODUCT 

def add_product():

    print("\n========== ADD PRODUCT ==========")

    product_id = input("Enter Product ID: ").strip().upper()

    if not product_id:
        print("Product ID cannot be empty!")
        return

    # Check duplicate Product 
    if product_id in products:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        if price <= 0 or quantity < 0:
            print("Invalid price or quantity!")
            return

    except ValueError:
        print("Please enter valid numeric values!")
        return

    print("\nAvailable Categories:")

    for category in categories:
        print("-", category)

    category = input("Enter Category: ").strip().title()

    if category not in categories:
        print("Invalid category!")
        return

    # Add product to dictionary
    products[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    # Update unique categories
    unique_categories.add(category)

    print("\nProduct added successfully!")


# 4. VIEW PRODUCTS 

def view_products():

    print("\n========== ALL PRODUCTS ==========")

    if not products:
        print("No products available!")
        return

    # Dictionary : Product IDs and prices
    product_prices = {
        product_id: details["price"]
        for product_id, details in products.items()
    }

    # Lambda: Sort products by price
    sorted_products = sorted(
        products.items(),
        key=lambda item: item[1]["price"]
    )

    # Display products
    for product_id, details in sorted_products:

        print("\nProduct ID:", product_id)
        print("Name:", details["name"])
        print("Price:", format_money(details["price"]))
        print("Stock:", details["quantity"])
        print("Category:", details["category"])

        print("------------------------------")

    print("\nProduct Price Dictionary:", product_prices)


# 5. SEARCH PRODUCT 
def search_product(product_id):

    product_id = product_id.strip().upper()

    if product_id in products:

        details = products[product_id]

        print("\n========== PRODUCT FOUND ==========")

        print("Product ID:", product_id)
        print("Name:", details["name"])
        print("Price:", format_money(details["price"]))
        print("Stock:", details["quantity"])
        print("Category:", details["category"])

        return details

    else:
        print("\nProduct not found!")
        return None


# 6. SELL PRODUCT 

def sell_product():

    print("\n========== SELL PRODUCT ==========")

    product_id = input("Enter Product ID: ").strip().upper()

    # Check if product existes
    if product_id not in products:
        print("Product not found!")
        return

    details = products[product_id]

    print("\nProduct:", details["name"])
    print("Available Stock:", details["quantity"])
    print("Price:", format_money(details["price"]))

    try:
        quantity = int(input("\nEnter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid quantity!")
        return

    # Check if stocks are available 
    if quantity > details["quantity"]:
        print("\nInsufficient stock!")
        print("Available Quantity:", details["quantity"])
        return

    # Calculate the bill
    subtotal = details["price"] * quantity

    # Placeholder for a future discount policy
    discount = 0

    if subtotal >= 5000:
        pass  # No discount policy is applied here.

    total = subtotal - discount

    # Reduce product stock
    details["quantity"] -= quantity

    # Store sale in sales list
    sales.append({
        "product_id": product_id,
        "product_name": details["name"],
        "quantity": quantity,
        "price": details["price"],
        "total": total
    })

    # Generate bill
    print("\n===================================")
    print("             CUSTOMER BILL")
    print("===================================")

    print("Product ID:", product_id)
    print("Product:", details["name"])
    print("Quantity:", quantity)
    print("Price Per Unit:", format_money(details["price"]))

    print("-----------------------------------")

    print("Subtotal:", format_money(subtotal))
    print("Discount:", format_money(discount))
    print("Total Amount:", format_money(total))

    print("===================================")
    print("       SALE COMPLETED!")
    print("===================================")

    print("Remaining Stock:", details["quantity"])


# ==========================================================
# 7. LOW STOCK FUNCTION
# ==========================================================

def low_stock():

    print("\n========== LOW STOCK REPORT ==========")

    # List: Find products with stock below 5
    low_stock_products = [
        (product_id, details)
        for product_id, details in products.items()
        if details["quantity"] < 5
    ]

    if not low_stock_products:
        print("No low-stock products found!")
        return

    for product_id, details in low_stock_products:

        print(
            details["name"],
            "-",
            details["quantity"],
            "remaining"
        )

# 8. SALES SUMMARY 

def sales_summary():

    print("\n========== SALES SUMMARY ==========")

    if not sales:
        print("No sales have been made yet!")
        return

    # Calculate total transactions
    total_transactions = len(sales)

    # Calculate total items sold using recursion
    total_items = count_total_items(sales)

    # Calculate total sales amount
    total_sales = sum(record["total"] for record in sales)

    print("Total Transactions:", total_transactions)
    print("Total Products Sold:", total_items)
    print("Total Sales Amount:", format_money(total_sales))

    print("\n========== PRODUCT-WISE SALES ==========")

    # Nested loop: Process products and their sales records
    for product_id, details in products.items():

        quantity_sold = 0
        product_revenue = 0

        for record in sales:

            if record["product_id"] == product_id:

                quantity_sold += record["quantity"]
                product_revenue += record["total"]

        if quantity_sold > 0:

            print("\nProduct:", details["name"])
            print("Quantity Sold:", quantity_sold)
            print("Revenue:", format_money(product_revenue))


# 9. ADD MORE STOCK FUNCTION (EXTRA FEATURE)

def add_stock():

    print("\n========== ADD MORE STOCK ==========")

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id not in products:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter Quantity to Add: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid quantity!")
        return

    # Increase existing stock
    products[product_id]["quantity"] += quantity

    print("\nStock updated successfully!")

    print("Product:", products[product_id]["name"])
    print("New Available Stock:", products[product_id]["quantity"])


# 10. MAIN MENU FUNCTION

def main():

    while True:

        print("\n")
        print("======================================")
        print("        MINI SHOP MANAGEMENT")
        print("======================================")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Sell Product")
        print("5. Check Low Stock")
        print("6. Sales Summary")
        print("7. Add More Stock")
        print("8. Exit")

        print("======================================")

        choice = input("Enter your choice (1-8): ").strip()

        # Handle invalid input
        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("\nInvalid choice! Please select 1-8.")
            continue

        if choice == "1":

            add_product()

        elif choice == "2":

            view_products()

        elif choice == "3":

            product_id = input("Enter Product ID: ")
            search_product(product_id)

        elif choice == "4":

            sell_product()

        elif choice == "5":

            low_stock()

        elif choice == "6":

            sales_summary()

        elif choice == "7":

            add_stock()

        elif choice == "8":

            print("\nThank you for using Mini Shop System!")
            print("Exiting program...")

            break

# 11. PROGRAM EXECUTION

if __name__ == "__main__":
    main()

