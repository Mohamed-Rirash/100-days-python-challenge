import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")

image = "day25/a.gif"
screen.addshape(image)
turtle.shape(image)

name_turtle = turtle.Turtle()
name_turtle.penup()
name_turtle.hideturtle()
name_turtle.color("black")


df = pd.read_csv("day25/50_states.csv")
all_stats = df.shape[0]

score = 0

def display_state_name(x, y, state_name):
    name_turtle.goto(x, y)
    name_turtle.write(state_name, align="center", font=("Arial", 12, "normal"))


is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{score}/{all_stats}Guess the state", prompt="What is your guessed state: ").title()

    state_data = df[df['state'] == answer_state]
    if not state_data.empty:
        x_coordinate = state_data['x'].values[0]
        y_coordinate = state_data['y'].values[0]
        display_state_name(x_coordinate, y_coordinate, answer_state)
        score += 1
    else:
        is_game_on = False

