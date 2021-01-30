from turtle import Turtle, Screen
import random
from random_color import random_color_gen

tim = Turtle()
tim.pensize(10)
tim.speed("fast")
screen = Screen()
screen.colormode(255)


direction = [0, 90, 180, 270]

while 1 > 0:
    tim.forward(20)
    tim.pencolor(random_color_gen())
    tim.setheading(random.choice(direction))
