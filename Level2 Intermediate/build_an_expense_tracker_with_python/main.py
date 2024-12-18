"""
https://dailypythonprojects.substack.com/p/build-an-expense-tracker-with-python
Project Description
Create a command-line app to track daily expenses. The app allows users to add expenses, view a summary of all expenses, and calculate total spending for a given period. It's great for practicing file handling, date manipulation, and list/dictionary management.
"""
from prettytable import PrettyTable
from datetime import datetime
PROMPT = """Welcome to the Expense Tracker!
1. Add an expanse
2. View all expanses
3. Search expanses by date
4. Calculate total spend
5. Exit
Choose an option: """

# expense_list = [{
#     "date": "1990-08-09",
#     "category": "food",
#     "description": "Launch at a cafe",
#     "amount": 12.5
# }]
expense_list = []
def load_data():

    try:
        f = open("expenses.txt", "r")
        f.close()
    except FileNotFoundError:
        f = open("expenses.txt", "w")
        f.close()
    finally:
        expense_list.clear()
        with open("expenses.txt", "r") as fs:
            content = fs.readlines()
        for line in content:
            if len(line.split(',')) > 1:
                expense_list.append({
                    "date": line.split(',')[0],
                    "category": line.split(',')[1],
                    "description": line.split(',')[2],
                    "amount": line.split(',')[3]
                })

load_data()
while True:
    user_input = int(input(PROMPT))

    match user_input:
        case 1:
            date = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date, "%Y-%m-%d").date()
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense_list.append({"date": date,
                                 "category": category,
                                 "description": description,
                                 "amount": amount})
            print("Expense added successfully!")
        case 2:
            print("--- All Expanses ---")
            t = PrettyTable(["Date", "Category", "Description", "Amount"])
            for expanse in expense_list:
                t.add_row([expanse["date"],expanse["category"], expanse["description"], f"${expanse["amount"]}"])
            print(t)
        case 3:
            search_date = input("Enter date to search (YYYY-MM-DD): ")
            for expanse in expense_list:
                if expanse["date"] == search_date:
                    # print("Found expanse(s)")
                    t = PrettyTable(["Category", "Description", "Amount"])
                    t.add_row([expanse["category"], expanse["description"], f"${expanse["amount"]}"])
                    print(t)
        case 4:
            total_spent = 0
            for expanse in expense_list:
                total_spent += float(expanse["amount"])
            print(f"Total spent: {total_spent}")
        case 5:
            save_data = ""
            for expanse in expense_list:
                save_data += f"{expanse["date"]},{expanse["category"]},{expanse["description"]},{expanse["amount"]}\n"
            with open("expenses.txt", "w") as fs:
                fs.write(save_data)
            break
