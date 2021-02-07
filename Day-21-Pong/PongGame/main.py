from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from consts import SCREEN_BG_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, PADDLE_1, PADDLE_2

screen = Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title('Pong Game')
screen.tracer(0)
screen.listen()

ball = Ball()
paddle1 = Paddle(PADDLE_1)
paddle2 = Paddle(PADDLE_2)

screen.onkey(paddle1.move_up, 'Up')
screen.onkeypress(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')
screen.onkeypress(paddle1.move_down, 'Down')

screen.onkey(paddle2.move_up, 'w')
screen.onkeypress(paddle2.move_up, 'w')
screen.onkey(paddle2.move_down, 's')
screen.onkeypress(paddle2.move_down, 's')

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.ball_move()
    if paddle1.distance(ball) < 51 and ball.pos()[0] <= 360:
        print("Hi")
    if paddle2.distance(ball) < 51 and ball.pos()[0] < -340:
        print("Hi")

screen.exitonclick()
