import turtle
import pandas
from list_countries import data_obj

screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.bgpic(image)

game_on = True
score = 0
while game_on:
    question = screen.textinput(f"{score}/50  States Correct", "Write a state's name:")
    if question == 'exit':
        game_on = False
        file = pandas.DataFrame(data_obj)
        file.to_csv("results.csv")

    answer = question.split(' ')
    definitive_ans = ''
    if len(answer) > 1:
        definitive_ans = f"{answer[0].capitalize()} {answer[1].capitalize()}"
    else:
        definitive_ans = question.capitalize()

    if definitive_ans in data_obj:
        x_axis = data_obj[definitive_ans][0]
        y_axis = data_obj[definitive_ans][1]
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(int(x_axis), int(y_axis))
        turtle.write(definitive_ans)
        data_obj.pop(definitive_ans)
        score += 1

screen.exitonclick()