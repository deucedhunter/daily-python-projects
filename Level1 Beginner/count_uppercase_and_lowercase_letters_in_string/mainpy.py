"""
https://dailypythonprojects.substack.com/p/count-uppercase-and-lowercase-letters
Project Description
This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.
"""

text = "This Sentence Has Mixed CASE Letters!"
result = {
    "uppercase": 0,
    "lowercase": 0,
}
for letter in text:
    if letter.isupper():
        result["uppercase"] += 1
    elif letter.islower():
        result["lowercase"] += 1

print("The number of uppercase letters is:", result["uppercase"])
print("The number of lowercase letters is:", result["lowercase"])