from inventory import inventory
 
def add_product():
    # We ask the user if they want to register a product
    registerP = input("Do you want to register a product?: y/n ").lower()
 
    # The loop runs while the answer is "y"
    while registerP == "y":
        name = input("Enter product name: ").strip()
 
        # Price validation
        price = None
        # None is an empty value
        # I use it to tell the loop there is no valid data yet and it should keep asking
        while price is None:
            try:
                price = float(input("Enter product price: "))
            except ValueError:
                print("Error: invalid information, enter a decimal number")
 
        # Quantity validation
        quantity = None
        # Same as with price
        # Quantity starts as None (empty) so the loop keeps asking until it gets a valid number
        while quantity is None:
            try:
                quantity = int(input("Enter number of units: "))
            except ValueError:
                print("Error: invalid information, enter a whole number.")
 
        # We create the product dictionary and add it to the inventory
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        inventory.append(product)
        print("--------Product Registered--------")
 
        # We ask if they want to continue to decide if the loop repeats or ends
        registerP = input("Do you want to register another product?: y/n ").lower()
