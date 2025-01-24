"""
https://dailypythonprojects.substack.com/p/find-the-most-frequent-word-in-a


Project Description

Write a program that takes a list of words and finds the most frequently occurring one. Start by writing this list in the first line of your program:

words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

Expected Output
Your program should find the most frequent word and print out a message similar to the following where the most frequent word (i.e., “love“) is is mentioned.
"""
from collections import Counter
words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]
x = dict(Counter(words))

biggest = ["none", 0]
for k, v in x.items():
    if v>biggest[1]:
        biggest=k, v

print(f"The most frequent word is \"{biggest[0]}\" appearing {biggest[1]} times.")