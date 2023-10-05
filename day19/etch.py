from turtle import Turtle,Screen

# w = forward
# s = bacward
# a = left
# d = right
# c = clear

diin = Turtle()
screen = Screen()


def move_forward():
    diin.forward(15)

def Move_backward():
    diin.backward(15)

def move_left():
    new_heading = diin.heading() + 10
    diin.setheading(new_heading)


def move_right():
    new_heading = diin.heading() - 10
    diin.setheading(new_heading)

def clear_drawing():
    diin.clear()
    diin.home()




screen.listen()

screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=Move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear_drawing)






screen.exitonclick()

