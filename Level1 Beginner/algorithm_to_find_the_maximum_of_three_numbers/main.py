"""
https://dailypythonprojects.substack.com/p/algorithm-to-find-the-maximum-of

Project Description
This program defines three numbers and determines which one is the largest. It then displays the largest number.
"""

num1 = 12
num2 = 45
num3 = 32

biggest_num = num1
if num2 > num1:
    biggest_num = num2
elif num3 > num2:
    biggest_num = num3
else:
    biggest_num = num1

print(F"The largest number is {biggest_num}")