from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="pong")

screen.tracer(0)


screen.listen()

insem = True

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.downward, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.downward, key="s")



game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(ball.move_speed)
    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce_Y()
    if ball.distance(r_paddle) < 100 and ball.xcor() > 340 or ball.distance(l_paddle) < 100 and ball.xcor() < -340 :
        ball.bounce_X()

    if ball.xcor() >= 400 :
        ball.ball_reset()
        scoreboard.lpoint()

    if  ball.xcor() <-400 :
        ball.ball_reset()
        scoreboard.rpoint()


    ball.move()


screen.exitonclick()