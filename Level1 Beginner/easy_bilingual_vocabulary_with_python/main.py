"""
https://dailypythonprojects.substack.com/p/build-a-bilingual-vocabulary-with-b03

How the Project Works:

(1) The program prompts the user to enter a word. The user enters “fish” and presses Enter.
(2) The program prompts the user to enter a translation for that word in a foreign language.
(3) The program repeats the process by prompting the user to enter another word.
(4) If the user enters “done”, the program closes and adds the data to a text file*.

"""


words = {}


def save_to_file():
    with open("data.txt", 'w') as fs:
        fs.write("Language 1 - Language 2\n")
        for key,value in words.items():
            fs.write(f"{key} - {value}\n")



while True:
    word_1 = input("Enter a word in Language 1 (or type 'done' to finish): ")
    if word_1 == "done":
        save_to_file()
        break
    word_2 = input(f"Enter the translation of '{word_1}' to Language 2: ")
    words[word_1] = word_2
