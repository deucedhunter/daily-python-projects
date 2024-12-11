"""
https://dailypythonprojects.substack.com/p/generate-random-person-name
Project Description
Create a program that reads a list of names from a text file, randomly picks one, and displays it. It's perfect for practicing file handling and working with lists in Python.

"""
import random
def read_from_file(path="names.txt"):

    with open(path, 'r') as fs:
        content = fs.readlines()

    for idx, name in enumerate(content):
        content[idx] = name.strip()
    return content


name_list = read_from_file()

print("Randomly selected name: ", random.choice(name_list))