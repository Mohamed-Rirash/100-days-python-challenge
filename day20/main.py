from turtle  import Screen
from snake import Snake
import time

#screen properties
screen =  Screen()
screen.bgcolor("black")
screen.setup(width=800,height=500)
screen.title("snake game")
screen.tracer(0)

# snake instance
snake = Snake()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)


   # move the snake 
while True:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()


   


    




screen.exitonclick()