"""
https://dailypythonprojects.substack.com/p/simple-dice-rolling-simulator

Project Description
This project simulates a dice roll by generating a random number between 1 and 6. Each time the program runs, it "rolls the dice" and displays the result. This project introduces students to working with random numbers and basic output formatting.
"""
from random import randint

print("You rolled a ", randint(1, 6))