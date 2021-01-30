from turtle import Turtle, Screen
tim = Turtle()
tim.speed('fast')
colors = ['red', 'magenta', 'aquamarine', 'purple', 'grey', 'crimson', 'olive', 'orange']


def move_forward_and_turn(deg, times):
    counter = 0
    while times > counter:
        tim.forward(50)
        tim.right(deg)
        counter += 1


start = 3
index = 0
while start <= 10:
    tim.pencolor(colors[index])
    index += 1
    degree = 360/start
    move_forward_and_turn(degree, start)
    start += 1


screen = Screen()
screen.exitonclick()
