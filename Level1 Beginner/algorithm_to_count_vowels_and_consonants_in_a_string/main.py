"""
https://dailypythonprojects.substack.com/p/algorithm-to-count-vowels-and-consonants
Project Description
This program defines a string, counts how many vowels and consonants are present, and displays both counts.
"""
text = "How many vowels and consonants are in this sentence?"
vowels = 0
consonants = 0
for letter in text.strip():
    if letter.lower() in "aeiou":
        vowels+=1
    elif letter.isalpha() :
        consonants+=1

print(f"The number of vowels in the string is: {vowels}")
print(f"The number of consonants in the string is: {consonants}")