from turtle import Turtle,Screen,colormode
import random
diin = Turtle()
colormode(255)

# random color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

diin.speed("fastest")
#draw a circle
def draw_circle():
    diin.circle(150)

# change the position
def draw_spirograph(soze_of_gap):
        
    for i in range(round(360 / soze_of_gap)):
        diin.color(random_color())
        draw_circle()
        current_heading = diin.heading()
        diin.setheading(current_heading +soze_of_gap)
        draw_circle()




draw_spirograph(5)


screen = Screen()
screen.exitonclick()