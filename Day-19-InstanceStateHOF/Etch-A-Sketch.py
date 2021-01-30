from tim_turtle import tim, screen


def move_fd():
    tim.fd(20)


def move_bd():
    tim.bk(20)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bd)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()