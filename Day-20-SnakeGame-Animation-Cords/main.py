from turtle import Screen
import time
from Snake_Game.snake_class import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snakes = []
for x in range(10):
    snakes.append(Snake(x_pos=0 - (x * 20), y_pos=0))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for x in range(len(snakes)):
        snakes[x].turtle.forward(20)
        if snakes[x].turtle.pos() >= (270, 0):
            game_is_on = False

turn_left = True
while turn_left:
    snakes[0].turtle.left(90)
    for x in range(1, len(snakes)-1):
        snakes[x].turtle.setpos(snakes[x+1].turtle.pos())
        snakes[0].turtle.forward(20)
    turn_left = False



screen.exitonclick()

