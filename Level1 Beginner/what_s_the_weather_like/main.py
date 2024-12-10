"""
https://dailypythonprojects.substack.com/p/whats-the-weather-like
Project Description

Create a program that asks the user about the current weather and, using a dictionary for decision-making, suggests an activity.

Start the script with this dictionary on top of your script:

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

Then, add more code so the program produces the following output.

"""
weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}
PROMPT = """What's the weather like today?
1. Sunny ☀️
2. Rainy 🌦️
3. Cloudy ☁️
4. Snowy ❄️
Choose 1, 2, 3, or 4: """
try:
    user_input = input(PROMPT)
    print(weather_activities[user_input])
except KeyError:
    print("Sorry, I there was no such weather option.")