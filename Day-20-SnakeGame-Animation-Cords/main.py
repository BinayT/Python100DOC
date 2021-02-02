from turtle import Screen
import time
from Snake_Game.snake_class import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snakes = []
for x in range(3):
    snakes.append(Snake(x_pos=0 - (x * 20), y_pos=0))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for x in range(len(snakes)-1, 0, -1):
        snakes[x].turtle.goto(snakes[x-1].turtle.pos())

    snakes[0].turtle.forward(20)
    if snakes[0].turtle.pos() >= (270, 0) and snakes[0].turtle.heading() == 0:
        snakes[0].turtle.left(90)






screen.exitonclick()

