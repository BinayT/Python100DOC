from turtle import Turtle


def create_line(height):
    half_height = int(height) / 2
    turtle = Turtle()
    turtle.color('white')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, half_height)
    turtle.pendown()
    turtle.setheading(270)
    turtle.speed('fastest')

    while turtle.pos()[1] > -half_height:
        turtle.fd(20)
        turtle.penup()
        turtle.fd(20)
        turtle.pendown()