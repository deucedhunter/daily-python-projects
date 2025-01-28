"""
https://dailypythonprojects.substack.com/p/check-if-number-is-positive-or-negative-332

Project Description

In a previous project, we created a program that checked if a number was positive or negative, or zero:

number = float(input("Enter a number: "))

if number > 0:
  print("The number is positive.")
elif number < 0:
  print("The number is negative.")
else:
  print("The number is zero.")

In this project, your task is to improve that project by:

(1) Doing the checks inside a function definition and then calling that function.

(2) Including the number in the messages (e.g., “The number -5 is negative”) as shown in the Expected Output section.
"""


def check_number(num):
    if number > 0:
        print(f"The number {num} is positive.")
    elif number < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")

number = int(input("Enter a number: "))
check_number(number)
