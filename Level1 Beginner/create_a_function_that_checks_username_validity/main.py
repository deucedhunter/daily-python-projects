"""
https://dailypythonprojects.substack.com/p/create-a-function-that-checks-username
Project Description

This program creates a function that checks whether a username is valid based on some simple rules. The function will take a username as input and return whether it is valid or not. The rules for a valid username are:

    The username must be between 5 and 15 characters.

    It must contain only alphanumeric characters (letters and numbers).

    It must start with a letter.
"""
validate = {
    "length": False,
    "isAlphanumeric": False,
    "isStartsWithLetter": False
}



def check_username_validity(username):
    error_list = []
    if 5<=len(username)<=15:
        validate["length"] = True
    else:
        error_list.append("Username must be between 5 and 15 characters.")
    non_alphanumeric = 0
    for idx, char in enumerate(username):
        if not char.isalnum():
            non_alphanumeric += 1
        if idx == len(username) - 1 and non_alphanumeric==0:
            validate["isAlphanumeric"] = True
        elif  idx == len(username) - 1 and non_alphanumeric>0:
            validate["isAlphanumeric"] = False
            error_list.append("Username must be alphanumeric.")
    if not username[0].isalpha():
        validate["isStartsWithLetter"] = False
        error_list.append("Username must start with a letter.")
    else:
        validate["isStartsWithLetter"] = True
    for error in error_list:
        print(error)


check_username_validity("aas#$%dsadas")