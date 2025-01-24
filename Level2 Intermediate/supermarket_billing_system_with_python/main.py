"""
https://dailypythonprojects.substack.com/p/supermarket-billing-system-with-python


Create a command line program that simulates a basic billing system for a supermarket. The user can input items purchased (e.g., butter, eggs, etc), their prices, and quantities. The app will calculate the total bill, apply any applicable discounts, and display an itemized bill summary. This project focuses on loops, dictionaries, and arithmetic calculations.

"""

bill = {}
PROMPT = """Welcome to the Supermarket Billing System!
Enter the number of items: """

num_items = int(input(PROMPT))

for n in range(0, num_items):
    print(f"Item {n+1}:")
    name = input("Name: ")
    price = float(input("Price per unit: "))
    quantity = input("Quantity: ")
    bill[n] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

print("--- Bill Summary ---")
sub_total = 0
for item in bill:
    summary = bill[item]["price"] * float(bill[item]["quantity"])
    print(f'{bill[item]["name"]}: {bill[item]["quantity"]} x {bill[item]["price"]} = {summary}')
    sub_total+=summary
print(f"Subtotal: ${round(sub_total, 2)}")
print("Discount: $0.00")
sales_tax = round(sub_total*0.05, 2)
print(f"Sales Tax (5%)", sales_tax)
total = round(sales_tax+sub_total, 2)
print(f"Total: ${total}")
print("Thank you for shopping with us!")