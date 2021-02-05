from turtle import Turtle, Screen
import time
from assets import create_line
from paddle import Paddle
SCREEN_BG = 'black'
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
POSITION1 = [(-450, 20), (-450, 0), (-450, -20)]
POSITION2 = [(442, 20), (442, 0), (442, -20)]

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, starty=0)
screen.bgcolor(SCREEN_BG)

screen.listen()

create_line(SCREEN_HEIGHT)
paddle = Paddle()
screen.onkey(paddle.move_up, 'Up')

# game_on = True
# while game_on:screen.onkey()
#     time.sleep(1)
#     screen.update()
#     game_on = False

screen.exitonclick()