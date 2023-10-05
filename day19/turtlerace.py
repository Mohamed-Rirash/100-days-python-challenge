from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "black", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]

is_race_on = False
all_turtles = []
winning_color = None

screen = Screen()
screen.setup(width=800, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\nred, green, blue, black, purple, orange ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-370, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 370:
            winning_color = turtle.pencolor()
            is_race_on = False

if winning_color == user_bet:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"Sorry, the {winning_color} turtle won. You lost.")

screen.exitonclick()
