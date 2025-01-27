"""
https://dailypythonprojects.substack.com/p/deadline-checker


Project Description
This program helps you keep track of deadlines by allowing you to input a specific date and time. It calculates whether the deadline has already passed, is happening today, or how many days remain until the deadline.
"""
import datetime

deadline = input("Enter the deadline (e.g. 2024-11-15 17:00): ")
deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
now = datetime.datetime.now()


deadline = datetime.datetime.timestamp(deadline)
now = datetime.datetime.timestamp(now)
days = int((deadline-now)/86400)
if days<0:
    print("The deadline has passed")
elif days == 0:
    print(f"The deadline is today. Keep working!")
else:
    print(f"The deadline is in {int(days)} day(s). Keep working!")