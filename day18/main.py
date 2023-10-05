from turtle import Turtle,Screen,colormode
import random

color_list = [(238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

#color
colormode(255)

#

diin = Turtle()
diin.shape("arrow")
diin.speed("fastest")
diin.penup()
diin.hideturtle()

diin.setheading(233)
diin.forward(300)
diin.setheading(0)
number_of_dofts = 100
for dot_count in range(1, number_of_dofts + 1): 

    diin.dot(20,random.choice((color_list)))
    diin.forward(50)


    if dot_count % 10 == 0:
        diin.setheading(90)
        diin.forward(50)
        diin.setheading(180)
        diin.forward(500)
        diin.setheading(0)

screen = Screen()
screen.exitonclick()