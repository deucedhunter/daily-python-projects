"""
https://dailypythonprojects.substack.com/p/count-any-word-in-a-book
Create a Python program to count the occurrences of any given word in the book stored in this text file.

"""
"""
Expected Output
The user can enter any word (e.g., snow), and the program should find out how many occurrences of that word exist in the book.txt 
"""

def load_from_file_2_list(file_name="files/book.txt"):
    """Load data from text file and save it as list"""
    with open(file_name, "r", encoding="utf-8") as fs:
        file_content = fs.readlines()
    return file_content

def load_content_from_file(file_name="files/book.txt"):
    with open(file_name, "r", encoding="utf-8") as fs:
        file_content = fs.read()
    return file_content

def count_term_in_text(word_to_count, text):
    """Move line by line, word by word and find all occurrences"""
    occur = 0
    for line in text:
        for word in line.split():
            if word.lower() == word_to_count:
                occur += 1
    return occur

def count_at_once(word_to_count, text):
    return text.count(word_to_count+" ")


search_term = input("Enter word to count in book: ")
# solution 1 work on lists
# book = load_from_file_2_list()
# occurrences = count_term_in_text(search_term, book)
# solution 2 work on string
book = load_content_from_file(file_name="files/book.txt")
occurrences = count_at_once(search_term, book)
print(occurrences)