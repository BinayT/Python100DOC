from turtle import Screen
from paddle import Paddle
from consts import SCREEN_BG_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

screen = Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title('Pong Game')
screen.listen()

paddle = Paddle()

screen.onkey(paddle.move_up, 'Up')
screen.onkeypress(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')
screen.onkeypress(paddle.move_down, 'Down')

screen.exitonclick()
