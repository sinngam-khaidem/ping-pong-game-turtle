from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from margin import Margin
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
margin = Margin()

screen.listen()
screen.onkey(key='Up', fun=r_paddle.go_up)
screen.onkey(key='Down', fun=r_paddle.go_down)
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)

is_game_on = True
while is_game_on:
    time.sleep(0.02 )
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_dir_wall()
    if r_paddle.distance(ball) < 75 or l_paddle.distance(ball) < 75:
        ball.change_dir_pad()

    if ball.xcor() < -365:
        scoreboard.r_score += 1
        scoreboard.clear()
        scoreboard.update_scores()
        ball.reset_ball()
        time.sleep(1)

    if ball.xcor() > 365:
        scoreboard.l_score += 1
        scoreboard.clear()
        scoreboard.update_scores()
        ball.reset_ball()
        time.sleep(1)




screen.exitonclick()
