"""
https://dailypythonprojects.substack.com/p/find-the-longest-word-in-a-list
Project Description

Write a program that takes a list of words and finds the longest word in that list. The program should also display the length of that word.

Start by placing the following list in your script:

words = ["apple", "banana", "cherry", "blueberry"]

Below is what your program should output.

As you can see above, the program has found the longest word and it has printed out a message which also includes the length of the longest word. It is recommended to use an f-string to construct that message.
"""

words = ["apple", "banana", "cherry", "blueberry"]
longest_word_idx = 0
for idx, word in enumerate(words):
    if len(word) > len(words[longest_word_idx]):
        longest_word_idx = idx

print(f"{words[longest_word_idx]} is the longest word with {len(words[longest_word_idx])} characters.")