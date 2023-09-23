from turtle import Turtle, Screen
import random

# Create a turtle object
diin = Turtle()
diin.shape("circle")
diin.speed("fast")  # Set the drawing speed to the fastest

diin.penup()
diin.goto(0, 200)
diin.pendown()

diin.pensize(2)

triangle_angle = 120
square_angle = 90
pentagon_angle = 72
hexagon_angle = 60
heptagon_angle = 51.5
octagon_angle = 45
nonagon_angle = 40
decagon_angle = 36

color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Cyan", "Magenta", "Lime", "Brown", "Gray"]

def set_random_color():
    random_color = random.choice(color_names)
    diin.color(random_color)

def triangle():
    set_random_color()
    for _ in range(3):
        diin.forward(180)
        diin.right(triangle_angle)

def square():
    set_random_color()
    for _ in range(4):
        diin.forward(180)
        diin.right(square_angle)

def pentagon():
    set_random_color()
    for _ in range(5):
        diin.forward(180)
        diin.right(pentagon_angle)

def hexagon():
    set_random_color()
    for _ in range(6):
        diin.forward(180)
        diin.right(hexagon_angle)

def heptagon():
    set_random_color()
    for _ in range(7):
        diin.forward(180)
        diin.right(heptagon_angle)

def octagon():
    set_random_color()
    for _ in range(8):
        diin.forward(180)
        diin.right(octagon_angle)

def nonagon():
    set_random_color()
    for _ in range(9):
        diin.forward(180)
        diin.right(nonagon_angle)

def decagon():
    set_random_color()
    for _ in range(10):
        diin.forward(180)
        diin.right(decagon_angle)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()
