"""
https://dailypythonprojects.substack.com/p/string-manipulations-on-user-input

Project Description

In this project, you will create a simple program that asks the user to enter their full name, and the program will perform several operations to the user entry as described in the “How Project Works” section further below.
How the Project Works

(1) First your program prompts the user to enter their name (first and last) in the terminal
(2) The user types in their name.
(3) Then, your program displays the user’s name in uppercase and then in lowercase.
(4) Next, the total number of characters is displayed.
(5) Lastly, the program reverses the user’s name and displays it.
"""

name = input("Please enter your full name: ")
print("Your name in uppercase: ", name.upper())
print("Your name in lowercase: ", name.lower())
split = name.split(" ")
print("total number of characters (excludiong spaces): ", len(split[0])+len(split[1]))
print("Your name reversed: ", name[::-1])
