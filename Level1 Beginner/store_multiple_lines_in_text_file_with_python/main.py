"""
https://dailypythonprojects.substack.com/p/level-2-intermediate-beginner

Project Description
Create a program that stores data in a text file.

How the Project Works

(1) Your program should ask the user to enter three sentences:

(2) Once the user has submitted the sentences, the program prints out a message saying that the sentences have been saved in a text file.

(3) The sentences are stored in a text file and there should be dash lines between the sentences. Here is what the text file should look like:
"""

sentences = ""
for i in range(3):
    sentence = input(f"Enter sentence {i+1}: ")
    if i < 2:
        sentences += sentence + "\n-----------\n"
    else:
        sentences += sentence
print("Sentences have been saved to user_sentences.txt.")

with open("user_sentences.txt", "w") as fs:
    fs.write(sentences)