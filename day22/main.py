from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time






screen = Screen()
screen.bgcolor("black")
screen.title("Pong game")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=l_paddle.go_up, key="w")






game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision on a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce the ball
        ball.y_bounce()
    # detect collision on a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect when paddle misses 
    if ball.xcor() > 380:        
        ball.starting_point()
        score.l_poin()
        
    

    if ball.xcor() < -380:        
        ball.starting_point()
        score.r_poin()

    
screen.exitonclick()


