"""
https://dailypythonprojects.substack.com/p/real-estate-price-estimator
Project Description
This is a simple beginner project where the program estimates the price of a property based on the size of the house (in square feet) and its location (city or suburb). The program will help practice basic Python concepts such as user input, conditional statements, and basic calculations.
"""

print("Welcome to the Real Estate Price Estimator!")
size_square = float(input("Enter the size of the property in square foot: "))
city_or_suburb = input("Enter the location (city or suburb): ").lower()
if city_or_suburb == "city":
    price = size_square * 250
elif city_or_suburb == "suburb":
    price = size_square * 100
else:
    print("You entered an invalid type of house location.")
    exit()


print(f"The estimated price for a {size_square} sq ft property im the city is : ${price:,}")