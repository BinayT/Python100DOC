from turtle import Screen
import time

from Snake_Game.snake_class import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
# snakes = []
# for x in range(10):
#     snakes.append(snake(x_pos=0 - (x * 20), y_pos=0))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for x in range(len(snakes)-1, 0, -1):
    #     snakes[x].goto(snakes[x-1].pos())
    #
    # snakes[0].forward(20)
    # if snakes[0].pos() >= (270, 0):
    #     snakes[0].left(90)


screen.exitonclick()

