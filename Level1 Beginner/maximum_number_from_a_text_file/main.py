"""
https://dailypythonprojects.substack.com/p/maximum-number-from-a-text-file

Project Description

In a previous project, we created a program that prompted the user to submit three numbers in the terminal and then the program returned the maximum number. For this project, instead of getting the numbers from the terminal, we will get them from a text file.
"""

num_list = []

with open("numbers.txt", "r") as fs:
    num_list = fs.readlines()

num_list = [int(num.strip()) for num in num_list]
max_num = max(num_list)

print("The maximum number in the file is: ", max_num)