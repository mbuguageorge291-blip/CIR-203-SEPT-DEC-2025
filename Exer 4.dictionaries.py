
inventory = {
    "Laptop": 15,
    "Smartphone": 8,
    "Headphones": 25,
    "Keyboard": 12,
    "Mouse": 5
}
inventory["Tablet"] = 10               
inventory["Mouse"] = 7                 


def low_stock_items(stock_dict):
    return {product: qty for product, qty in stock_dict.items() if qty < 10}

low_stock = low_stock_items(inventory)
print("Low Stock Products:", low_stock)


del inventory["Keyboard"]             
print("Updated Inventory:", inventory)


print("Inventory List:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")
