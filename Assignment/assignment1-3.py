#Lauren Song
#U79789182
#Area of composite shape

p = int(input('Enter the first diagonal length :'))
q = int(input('Enter the second diagonal length :'))
r = int(input('Enter the radius of the enclosed circle :'))

import math
pi = (math.pi)

#The area of a kite
area_kite = (p * q) / 2
#The area of a circle
area_circle = pi * (r**2)
#The shaded area
shaded_area = area_kite - area_circle

print(f'The shaded area is {shaded_area :.3f} square units.')
