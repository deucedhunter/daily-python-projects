"""
https://dailypythonprojects.substack.com/p/area-and-perimeter-calculator
Project Description

The objective of this project is to create two Python functions -one that calculates the area and one that calculates the perimeter of a rectangle.

How the Project Works

(1) Create a rectangle_area function that has two parameters: width and height. The function should calculate the area of the rectangle and return it using a return statement.

(2) In the same script, create a rectangle_perimeter function that has two parameters: width and height. The function should calculate the perimeter of the rectangle and return it using a return statement.

(3) Call the two functions by using some sample values (e.g., 10 for width and 3 for height) as arguments for width and height and print out the output.
"""

def rectangle_area(width, height):
    return width*height

def rectangle_perimeter(width, height):
    return 2*width+2*height


print(rectangle_area(10,3))
print(rectangle_perimeter(10,3))