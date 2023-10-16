import random
import turtle

print(random.randint(1, 6))

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

    
##import random as rn
val_list = [1,2,'three', 4.0, False]
r = rn.choice(val_list)
print(f"Here's a list: {val_list}")
print(f"and here's a random value from that list: {r}")
