from turtle  import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#screen properties
screen =  Screen()
screen.bgcolor("black")
screen.setup(width=800,height=800)
screen.title("snake game")
screen.tracer(0)

# snake instance and food instance
snake = Snake()
food = Food()
score = ScoreBoard()

#controling the snake
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)


   # move the snake 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()


    # detect collision with 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 395 or snake.head.ycor() < -395:
        game_is_on = False
        score.game_over()
   
    # detect collition with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


    




screen.exitonclick()