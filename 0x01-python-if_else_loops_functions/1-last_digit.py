#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = -last

if last == 0:
    str = "0"
elif last > 5:
    str = "greater than 5"
elif last < 6:
    str = "less than 6 and not 0"

print(f"Last digit of {number} is {last} and is {str}")
