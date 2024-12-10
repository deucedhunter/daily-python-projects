"""
https://dailypythonprojects.substack.com/p/check-if-number-is-positive-or-negative
Project Description

Create a simple program that checks if a given number is positive, negative, or zero.
Expected Output
Any time the program is executed, it prints out different messages based on the number sign:
"""


# Solution 1
# casting number to integer and treat as whole
# try:
#     number = int(input("Enter a number: "))
#     if number > 0:
#         print("The number is positive.")
#     elif number < 0:
#         print("The number is negative.")
#     else:
#         print("The number is zero.")
# except ValueError:
#     print("Program works only on numbers.")

# Solution 2
text = input("Enter a number: ")
if text[0] == '-':
    print("The number is negative.")
elif text != "0":
    print("The number is positive.")
else:
    print("The number is zero.")
