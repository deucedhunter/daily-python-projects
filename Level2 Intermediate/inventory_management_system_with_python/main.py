"""
https://dailypythonprojects.substack.com/p/inventory-management-system-with

Project Description
Build a command-line app that allows a small business to manage their inventory. The app will let users:
"""

inventory = {
    "Strong Glue XC":{
        "quantity": 14,
        "price": 3.99,
    }
}

PROMPT = """Welcome to the Inventory Management System!
1. Add new item
2. Update stock
3. View inventory
4. Search for an item
5. Exit
Choose an option: """

while True:
    user_input = input(PROMPT)
    match user_input:
        case "1":
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            item_price = float(input("Enter item price: "))
            item_list = list(inventory.keys())
            if item_name in inventory:
                print("Item already exists! Please choose update stock to change quantity")
            else:
                inventory[item_name] = {"quantity": item_quantity, "price": item_price}
        case "2":
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            item_price = float(input("Enter item price: "))
            item_list = list(inventory.keys())
            if item_name in inventory:
                inventory[item_name] = {"quantity": item_quantity, "price": item_price}
            else:
                print("Item does not exist! Please add it at first from add new item option")
        case "3":
            for item in inventory:
                print(f"{item.title()}: {inventory[item]['quantity']}, ${inventory[item]['price']}")
        case "4":
            item_name = input("Enter item name: ")
            item_list = list(inventory.keys())
            if item_name in list(inventory.keys()):
                print(f"Found: {item_name}: {inventory[item_name]['quantity']}, ${inventory[item_name]['price']}")
        case "5":
            break