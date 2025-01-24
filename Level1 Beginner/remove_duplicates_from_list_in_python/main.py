"""
https://dailypythonprojects.substack.com/p/remove-duplicates-from-list-in-python

Project Description

Write a program that removes duplicate items from a list while keeping the original order. The program should return a new list with only unique elements. You can place the following list in your script and then add the code that removes duplicates and prints out the new list.

numbers = [3, 1, 2, 3, 4, 1, 5, 2]

We provide two different solutions to this problem behind the “Show Code” button and compare the two discussing which is the best code.
Expected Output
The program should print out the text “List without duplicates:” followed by the cleaned list.

"""


numbers = [3, 1, 2, 3, 4, 1, 5, 2]
no_copies = []

# 1
# for num in numbers:
#     if num not in no_copies:
#         no_copies.append(num)
#

# 2
# no_copies = list(set(numbers))

#3
numbers.sort()
for num in range(len(numbers)):
    if num+1 < len(numbers):
        if numbers[num] == numbers[num+1]:
            numbers.pop(num + 1)
no_copies = numbers

print(no_copies)