###week 3 lecture 2
###compound assignment recap
##
##number = 20;x =5; y =6 #;(semi)used for statement separation, not statement termination
##
##number *= x+y #number = number * (x+y) = 20 * (5 + 6) = 20*11 = 220
##print(f'number is {number}')
##number -= 10
##print(f'number is {number}')
##number /= 7
##print(f'number is {number}')
##number //= 4 #number = number // (4) = 30.0 // 4 = 7
##print(f'number is {number}')
##number %= 10 #number = number % (10) = 7.0 % 10 = 7.0
##print(f'number is {number}')
##number **= 3
##print(f'number is {number}')

#importing modules
import math,random

num = float(input('Enter a positive number:'))
sq = math.sqrt(num)
print(f'The square root of {num} is {sq:.3f}')

r = random.randint(1,6)
print(f"Here's a random number between 1 and 6: {r}")

from math import ceil,fabs #import the method
print(f'{num} rounded up is {ceil(num)}')
print(f'The absolute value of {num} is {fabs(num)}')

##
##import random as rn
##val_list = [1,2,'three', 4.0, False]
##r = rn.choice(val_list)
##print(f"Here's a list: {val_list}")
##print(f"and here's a random value from that list: {r}")

#selction
#relational: <,>,<=,>=,==,!=
#logical: and,or, not

##temp = int(input('Temperature?'))
##rain = input('Raining? (yes or no)')
##
##if rain == 'yes':
##    raining = True
##else:
##    raining = False
##
##if temp > 70 and not raining:
##    print('Go hiking')
##else:
##    print('Stay inside')
##
###using if elif else
##score = float(input('Enter a score:'))
##if score >= 80:
##    print('Yay!')
##    print('You advance!')
##elif score >=0 and score <80:
##    print('Oh no!')
##    print('Try again')
##else:
##    print("That's an invalid score.")
##    








