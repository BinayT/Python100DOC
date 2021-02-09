from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

BALL_X_MAX = 330
SCREEN_BG_COLOR = 'black'
PADDLE_1_POS = (350, 0)
PADDLE_2_POS = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(SCREEN_BG_COLOR)
screen.tracer(0)
screen.listen()

paddle1 = Paddle(PADDLE_1_POS)
paddle2 = Paddle(PADDLE_2_POS)
ball = Ball()
scoreboard = Scoreboard()
ball.create_line()

screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle2.up, 'w')
screen.onkeypress(paddle1.up, 'Up')
screen.onkeypress(paddle2.up, 'w')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.down, 's')
screen.onkeypress(paddle1.down, 'Down')
screen.onkeypress(paddle2.down, 's')

game_sleep_time = 0.1
score1 = 0
score2 = 0
game_on = True
while game_on:
    time.sleep(game_sleep_time)
    screen.update()
    ball.move()
    scoreboard.update_score(score1, score2)
    if ((ball.xcor() >= BALL_X_MAX and (paddle1.ycor() + 60 > ball.ycor() > paddle1.ycor() - 60)) or
            (ball.xcor() <= -BALL_X_MAX and (paddle2.ycor() + 60 > ball.ycor() > paddle2.ycor() - 60))):
        ball.bounce_paddle()
        game_sleep_time -= 0.003

    if -360 > ball.xcor() < 0:
        ball.goto(0, 0)
        game_sleep_time = 0.1
        score2 += 1
    if 0 < ball.xcor() > 360:
        ball.goto(0, 0)
        game_sleep_time = 0.1
        score1 += 1



screen.exitonclick()