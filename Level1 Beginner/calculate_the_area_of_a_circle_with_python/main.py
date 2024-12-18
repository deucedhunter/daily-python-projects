"""
https://dailypythonprojects.substack.com/p/calculate-the-area-of-a-circle-with
Project Description
Your task for today is to create a Python program that calculates the area of a circle.

"""
import math

radius = float(input("Enter the radius of the circle: "))

area =  math.pi * (radius * radius)

print(f"The are of the circle with radius {radius} is {round(area, 2)}.")