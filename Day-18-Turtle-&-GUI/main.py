from turtle import Turtle, Screen
tim = Turtle()


def dashed():
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()


def dash_5_times():
    counter = 0
    while counter != 5:
        counter += 1
        dashed()


def square():
    counter = 0
    while counter != 4:
        counter += 1
        dash_5_times()
        tim.left(90)


tim.shape("turtle")
tim.fillcolor("LemonChiffon")
tim.pencolor("red")
square()

screen = Screen()
screen.exitonclick()

