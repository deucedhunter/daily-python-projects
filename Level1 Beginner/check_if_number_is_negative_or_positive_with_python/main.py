"""
https://dailypythonprojects.substack.com/p/check-if-number-is-negative-or-positive

Project Description
This program asks the user to input a number and checks whether it is positive, negative, or zero.
"""

user_number = int(input("Enter a number: "))

if user_number < 0:
    print("The number you entered is negative.")
elif user_number > 0:
    print("The number you entered is positive.")
else:
    print("The number you entered is zero.")