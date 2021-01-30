from turtle import Turtle, Screen
from random_color import random_color_gen

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


def draw_spirograph(qty, radius):
    counter = 0
    while counter <= 360:
        tim.pencolor(random_color_gen())
        tim.circle(radius)
        counter += qty
        tim.setheading(counter)


draw_spirograph(3, 70)

screen.exitonclick()