import math,random

num = float(input('Enter a positive number:'))
sq = math.sqrt(num)
print(f'The square root of {num} is {sq:.3f}')

r = random.randint(1,6)
print(f"Here's a random number between 1 and 6: {r}")

from math import ceil,fabs #import the method
print(f'{num} rounded up is {ceil(num)}')
print(f'The absolute value of {num} is {fabs(num)}')
