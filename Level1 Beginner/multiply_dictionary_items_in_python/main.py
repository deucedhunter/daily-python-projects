"""
https://dailypythonprojects.substack.com/p/multiply-dictionary-items-in-python
Project Description

This project starts with a pre-defined dictionary representing a grocery list with quantities:

grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

You task is to add some code that updates all the values of the dictionary by multiplying them by 10. Then, print out the updated dictionary.
"""

grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

# Solution 1
# unpacking key and value from grocery list and multiply values
# for key, value in grocery_list.items():
#     grocery_list[key] = value * 10
#
# Solution 1
# Use comprehension to multiply
# grocery_list = {k:v*10 for (k, v) in grocery_list.items()}
print(grocery_list)

