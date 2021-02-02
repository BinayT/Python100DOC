from turtle import Turtle


def snake(x_pos, y_pos):
    tim = Turtle('square')
    tim.penup()
    tim.color('white')
    tim.setpos(x_pos, y_pos)
    return tim