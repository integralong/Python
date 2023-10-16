### COP 2510 WEEK 6 LEC 1
##
### More with (for) loops
##for k in range(1000,99, -50):
##    print(f'{k}', end =' ')
##print()
##
###for loop with strings
##plan = 'Get some food after class.'
##for p in plan:
##    print(f'{p}', end ='-')
##print()
##
###for loop with lists
##names = ['Jinx', 'Vi', 5, 11, 'caitlyn']
##for n in names:
##    print(f'Hi {n}!')
##
###nested loops
##dig1 = 0
##while dig1 <= 9: #outer loop
##    dig2 = 0
##    #break
##    while dig2 <= 9: #inner loop
##        print(f'{dig1} -- {dig2}')
##        #break #inner loop is interrupted, but not the outer loop
##        dig2 += 1
##    dig1 += 1
##
###enumerate function
##for i, j in enumerate(range(1,11)):
##    print(f'{i} * {j} = {i * j}')


import turtle

#draw a regular polygon

sides = int(turtle.textinput('Dialog Box', 'Enter number of sides'))
length = int(turtle.textinput('Dialog Box', 'Enter length of sides'))
angle = ((sides - 2) * 180) / sides #calculated interior angle


for s in range(sides):
    turtle.forward(length) #fd - forward
    turtle.dot(5, 'green')
    turtle.right(180 - angle)

turtle.clearscreen()


#draw a series of circles

x,y = -300, 0
turtle.penup()
turtle.setpos(x,y)

nc = int(turtle.textinput('Dialog Box', 'How many circles to draw?'))

for z in range(nc):
    turtle.pendown()
    turtle.circle(60)
    x += 120
    turtle.penup()
    turtle.setpos(x,y)






























