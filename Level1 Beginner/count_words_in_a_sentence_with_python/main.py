"""
https://dailypythonprojects.substack.com/p/count-words-in-a-sentence-with-python

Project Description
This project involves creating a program that takes a sentence as input and counts the number of words in that sentence. The program will also identify the longest word in the sentence.
"""


def longest_word(sentence):
    longest_word = ""
    for word in sentence.split():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
sentence = input("Enter a sentence: ")
number_of_words_in_sentence = len(sentence.split())
print("The Longest Word in the Sentence is", longest_word(sentence))