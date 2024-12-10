"""
https://dailypythonprojects.substack.com/p/random-password-generator
Project Description
Create a command-line app that generates secure random passwords based on user preferences. The user can specify the password length and whether to include uppercase letters, numbers, and special characters. This project focuses on randomness, string operations, and user input validation.
"""
import random
def generate_password(length, isUpper, isNumbers, isSpecial):
    password = ""
    one_forth = int(length / 4)
    if isUpper.lower() == "yes":
        for i in range(one_forth):
            password+= chr(random.randint(65, 90))
    if isNumbers.lower() == "yes":
        for i in range(one_forth):
            password+= str(random.randint(0, 9))
    if isSpecial.lower() == "yes":
        for i in range(one_forth):
            password+= chr(random.randint(33, 47))

    lacking_chars = length - len(password)
    for i in range(lacking_chars):
        password += chr(random.randint(97, 122))
        random.shuffle(list(password))
    return password

print("Welcome to the Password Generator!")
pass_length = int(input("Enter desired password length (minimum 6): "))
pass_upper = input("Include uppercase letters? (yes/no): ")
pass_numbers = input("Include numbers? (yes/no): ")
pass_special = input("Include special characters? (yes/no): ")

password = generate_password(pass_length, pass_upper, pass_numbers, pass_special)

print(f"Generated password: {password}")
