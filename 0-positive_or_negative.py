#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
	print("0 is zero")
elif number > 0:
	print(f'{number} is positive')
elif number < 0:
	print(f'{number} is negative')
