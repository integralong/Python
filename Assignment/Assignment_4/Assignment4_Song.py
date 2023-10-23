#Lauren Song
#U79789182
#Tortoise vs. Hare

import turtle
import random
import time

def lt(t, angle):
    t.lt(angle)
def fd(t, num):
    t.fd(num)
def line_setting():
    t = turtle.Turtle()
    t.speed(0)

    t.up()
    t.goto(-100, 0)
    t.down()
    t.color("white")
    fd(t, 200)
    lt(t, 90)
    t.color("black")
    fd(t, 50)
    t.write("End")
    t.color("white")
    lt(t, 90)
    fd(t, 200)
    t.color("black")
    t.write("Start")
    lt(t, 90)
    fd(t, 50)
    lt(t, 90)
    t.up()
    t.goto(t.xcor()-50, t.ycor())
    t.up()
    
    t.hideturtle()



def image_setting():
    t_hare.shape("classic")
    t_tortoise.shape("turtle")

    t_hare.up()
    t_hare.shapesize(1,1)
    t_hare.speed(0)
    t_hare.goto(-100, 50)

    t_tortoise.up()
    t_tortoise.shapesize(0.5,0.5)
    t_tortoise.speed(0)
    t_tortoise.goto(-100, 0)

def update_tortoise_position(current_position):
    rng = random.randint(1, 10)
    if 1 <= rng <= 5:
        current_position += 3
    elif 6 <= rng <= 7:
        current_position -= 5
    else:
        current_position += 1

    if current_position < -100:
        current_position = -100
    if current_position > 100:
        current_position = 100
        
    return current_position

def update_hare_position(current_position):
    rng = random.randint(1, 10)
    if 1 <= rng <= 2:
        pass
    elif 3 <= rng <= 4:
        current_position += 7
    elif 5 <= rng <= 5:
        current_position -= 10
    elif 6 <= rng <= 8:
        current_position += 1
    else:
        current_position -= 2

    if current_position < -100:
        current_position = -100
    if current_position > 100:
        current_position = 100
        
    return current_position






def start():
    t_tortoise_x = -100
    t_hare_x = -100
    elapsed_time = 0
    while t_tortoise_x < 100 and t_hare_x < 100:
        t_hare_x = update_hare_position(t_hare_x)
        t_tortoise_x = update_tortoise_position(t_tortoise_x)

        t_hare.setx(t_hare_x)
        t_tortoise.setx(t_tortoise_x)
        elapsed_time += 1


            
        if t_tortoise_x >= 100 or t_hare_x >= 100:
            if t_tortoise_x > t_hare_x:
                text.penup()
                text.goto(120,25)
                text.pendown()
                text.color("black")
                text.write('Tortoise wins!')
                text.penup()
                text.goto(0, -50)
                text.pendown()
                text.write(f'\'Time\' of race: {int(elapsed_time)} \'seconds\'')
                text.hideturtle()
            elif t_tortoise_x < t_hare_x:
                text.penup()
                text.goto(120,25)
                text.pendown()
                text.color("black")
                text.write('Hare wins!')
                text.penup()
                text.goto(0, -50)
                text.pendown()
                text.write(f'\'time\' of race: {int(elapsed_time)} \'seconds\'')
                text.hideturtle()
            else:
                text.penup()
                text.goto(120,25)
                text.pendown()
                text.color("black")
                text.write('Tie!')
                text.penup()
                text.goto(0, -50)
                text.pendown()
                text.write(f'\'time\' of race: {int(elapsed_time)} \'seconds\'')
                text.hideturtle()
                
                break
                
t_hare = turtle.Turtle()
t_tortoise = turtle.Turtle()

screen = turtle.Screen()
text = turtle.Turtle()
text.speed(0)
text.hideturtle()
line_setting()
image_setting()
text.clear()
text.color("blue")

turtle.title("Tortiose vs Hare!")

start()

turtle.exitonclick()

