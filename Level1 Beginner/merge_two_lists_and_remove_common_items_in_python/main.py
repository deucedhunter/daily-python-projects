"""
Project Description

Let’s have another project on lists since they are a key data type in Python whenever we need to store multiple items.

Your task for today is to write a program that merges two lists into one and removes any common items between them.

Start by pasting these two lists in an empty Python script:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

Then, add some code so your program should:

    Merge these two lists into one single list.

    Remove the common/duplicate items

    Print out the updated list.
"""
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged = set(list1).symmetric_difference(set(list2))
to_list = list(merged)
print(to_list)
