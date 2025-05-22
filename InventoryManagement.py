# Inventory Management Program

# Initialize inventory with some items
inventory = [
    {"id": "001", "name": "Laptop", "quantity": 10, "price": 999.99},
    {"id": "002", "name": "Mouse", "quantity": 50, "price": 19.99},
    {"id": "003", "name": "Keyboard", "quantity": 30, "price": 49.99}
]

def display_inventory():
    print("\nCurrent Inventory:")
    print("{:<8} {:<15} {:<10} {:<10}".format("ID", "Item Name", "Quantity", "Price"))
    print("-" * 45)
    for item in inventory:
        print("{:<8} {:<15} {:<10} ${:<10.2f}".format(
            item["id"],
            item["name"],
            item["quantity"],
            item["price"]
        ))

def add_item():
    print("\nAdd New Item")
    while True:
        item_id = input("Enter item ID: ")
        # Check if ID already exists
        if any(item["id"] == item_id for item in inventory):
            print("Error: Item ID already exists!")
            return
        else:
            break
    
    name = input("Enter item name: ")
    
    # Quantity validation loop
    while True:
        quantity = input("Enter quantity: ")
        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break
        print("Invalid quantity! Please enter a positive integer.")
    
    # Price validation loop
    while True:
        price = input("Enter price: ")
        if price.replace('.', '', 1).isdigit() and float(price) > 0:
            price = float(price)
            break
        print("Invalid price! Please enter a positive number.")
    
    inventory.append({
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price
    })
    print("Item added successfully!")

def update_item():
    item_id = input("\nEnter item ID to update: ")
    for item in inventory:
        if item["id"] == item_id:
            # Update quantity
            while True:
                new_qty = input(f"Current quantity: {item['quantity']}. Enter new quantity: ")
                if new_qty.isdigit() and int(new_qty) >= 0:
                    item["quantity"] = int(new_qty)
                    break
                print("Invalid quantity! Please enter a non-negative integer.")
            
            # Update price
            while True:
                new_price = input(f"Current price: ${item['price']:.2f}. Enter new price: ")
                if new_price.replace('.', '', 1).isdigit() and float(new_price) >= 0:
                    item["price"] = float(new_price)
                    break
                print("Invalid price! Please enter a non-negative number.")
            
            print("Item updated successfully!")
            return
    print("Item ID not found!")

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Add New Item")
    print("3. Update Item")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        update_item()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-4.")