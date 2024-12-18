"""
https://dailypythonprojects.substack.com/p/generate-text-files-with-random-names

Project Description
Your task for today is to create a Python program which generates a new text file every time you run it.
"""
import random
import string

name = ""
for _ in range(10):
    name += random.choice(string.ascii_letters)

with open(name + ".txt", "w") as text_file:
    text_file.write(name)
