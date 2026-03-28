from inventory import inventory
 
def calculate_statistics():
    # If there are no products, there is nothing to calculate
    if not inventory:
        print("\nThere is no data to calculate statistics.")
        return
 
    total_value = 0
    total_units = 0
 
    # We go through the inventory adding price × quantity for each product
    for item in inventory:
        total_value += item['price'] * item['quantity']
        total_units += item['quantity']
 
    # We display the results clearly
    print("\n-----------------------------------")
    print("    GENERAL STATISTICS")
    print("------------------------------------")
    print(f"Total inventory value:     ${total_value:,.2f}")
    print(f"Total units:               {total_units}")
    print(f"Total distinct products:   {len(inventory)}")
    print("------------------------------------\n")
