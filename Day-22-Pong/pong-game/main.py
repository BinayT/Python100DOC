from turtle import Screen
from constants import SCREEN_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_COLOR, PADDLE_POS_A, PADDLE_POS_B
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
import time

screen = Screen()
screen.title(SCREEN_TITLE)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)


paddle_a = Paddle(PADDLE_POS_A)
paddle_b = Paddle(PADDLE_POS_B)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_a.move_up, 'Up')
screen.onkey(paddle_a.move_down, 'Down')
screen.onkey(paddle_b.move_up, 'w')
screen.onkey(paddle_b.move_down, 's')
screen.onkeypress(paddle_a.move_up, 'Up')
screen.onkeypress(paddle_a.move_down, 'Down')
screen.onkeypress(paddle_b.move_up, 'w')
screen.onkeypress(paddle_b.move_down, 's')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_score(ball.send_scores()[0], ball.send_scores()[1])
    ball.move(paddle_a, paddle_b)

screen.exitonclick()
