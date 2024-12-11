"""
https://dailypythonprojects.substack.com/p/daily-mood-booster
Project Description
Create a program that prompts the user to enter their mood (Happy, Stressed, or Tired) and display a message depending on the moood submitted by the user.
"""

mood_list = {
    "1": "That’s great, {name}! Keep streading your joy",
    "2": "Take a deep breath, {name}. You're doing amazing!",
    "3": "Rest up, {name}. Tomorrow is a fresh start!"
}

name = input("What is your name? ")
PROMPT = f"""Hi, {name} How are you feeling today?
1. Happy 😄
2. Stressed 😟
3. Tired 😩
Choose 1, 2, or 3: """
user_mood = input(PROMPT)
print(mood_list[user_mood].format(name=name))