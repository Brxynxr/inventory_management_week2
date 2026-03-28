from inventory import inventory
 
def show_inventory():
    # We check if the inventory is empty before going through it
    if not inventory:
        print("\nThe inventory is empty.")
    else:
        print("\n==============================")
        print("    REGISTERED PRODUCTS")
        print("==============================")
 
        # We go through each product in the inventory and display it on screen
        for item in inventory:
            print(f"Product: {item['name']} | Price: ${item['price']:,.2f} | Quantity: {item['quantity']}")
        print("------------------------------")
