inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 25,
    "Keyboard": 5,
    "Mouse": 12
}
print("Original Inventory:")
print(inventory)
inventory["Tablet"] = 20            
inventory["Phone"] = 10             
print("\nAfter Adding and Updating:")
print(inventory)
def low_stock_products(inv):
    return [product for product, qty in inv.items() if qty < 10]
print("\nProducts with stock less than 10:")
print(low_stock_products(inventory))
del inventory["Keyboard"]            
print("\nAfter Removing Discontinued Product:")
print(inventory)
print("\nInventory List:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")
