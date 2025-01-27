"""
https://dailypythonprojects.substack.com/p/copy-sum-up-two-numbers-from-user

Project Description
This program asks the user to enter their birth year and the current year. It then calculates and displays the user's age.

How the Project Works
(1) The program starts by asking the user to enter their birth year.
(2) Next, it asks the user to enter the current year.
(3) The program calculates the user's age by subtracting the birth year     from the current year.
(4) Finally, it displays a message in the terminal that includes the        calculated age.
"""

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

print(f"You are {current_year-birth_year} years old.")