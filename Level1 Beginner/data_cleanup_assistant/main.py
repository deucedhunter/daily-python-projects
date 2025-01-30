"""
https://dailypythonprojects.substack.com/p/data-cleanup-assistant

Project Description

For this project, you are provided with the following messy list of strings that represent names:

messy_names = [
    "  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]

Please place that list on top of your Python script. As you can see, some names are in lowercase letters, some have extra spaces, and others are duplicates.

Write a program that cleans the data by removing extra spaces, converting all names to title case, and removing any duplicates. Finally, display the cleaned list in alphabetical order.
"""

messy_names = [    "  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]
clean_names = set()
for name in messy_names:
    current_name = name.strip().title()
    clean_names.add(current_name)

clean_names = list(clean_names)
for name in clean_names:
    print(name)