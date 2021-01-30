# import tryy
# from turtle import Turtle,Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.fd(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon", "Type"]
table.add_row(['Pikachu', 'Electric'])
table.add_row(['Raichu', 'Electric'])
table.add_row(['Bulbasar', 'Land'])

table.align = 'l'

print(table)
