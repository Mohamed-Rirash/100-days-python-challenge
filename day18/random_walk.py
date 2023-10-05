# random color
# random move funcion
# 
from turtle import Turtle, Screen,colormode
import random

diin = Turtle()
# color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Cyan", "Magenta", "Lime", "Brown", "Gray"]
directions = [0, 90,180,270]
diin.pensize(10)

# diin.pensize(10)
# diin.speed("fastest")

# def random_colors():
#     random_color = random.choice(color_names)
#     diin.color(random_color)



# def movies():
#     for _ in range(150):
#         diin.forward(15)
#         random_direction = random.choice(directions)
#         diin.left(random_direction)
#         random_colors()


# movies()

# TODO 2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

for _ in range(200):
    diin.forward(30)
    diin.setheading(random.choice(directions))
    # add a color
    diin.color(random_color())

screen = Screen()
screen.exitonclick()