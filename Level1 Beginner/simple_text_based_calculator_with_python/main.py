"""
https://dailypythonprojects.substack.com/p/simple-console-calculator-add-subtract

Project Description
Build a program that the user to input two numbers and an operation (addition, subtraction, multiplication, or division). It performs the operation on the two numbers and displays the result.
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Enter operation (+, -, * or /): ")

result = 0
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _ :
        print("Operation not supported")
        exit()
print(f"The result is: {result}")