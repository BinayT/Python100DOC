from turtle import Screen
from consts import SCREEN_BG_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

screen = Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title('Pong Game')

screen.exitonclick()
