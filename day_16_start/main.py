# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.right(90)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable, MARKDOWN
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Arsen",])
table.add_column("Type", ["Electric", "Water", "Fire", "Water",])
table.add_column("Super Force", ["Yes", "No", "Yes", "Yes"])

table.align = "l"

print(table)