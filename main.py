from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(1366, 768)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-300, -200, -100, 0, 100, 200]
all_turtle = []
is_race_on = True

for turtle_number in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(500)
    new_turtle.color(colors[turtle_number])
    new_turtle.penup()
    new_turtle.goto(-673, position[turtle_number])
    all_turtle.append(new_turtle)

if user_bet:
    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 633:
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    print(f"You won. Congratulations the {winning_color} turtle won")
                else:
                    print(f"You lost. Sorry the {winning_color} turtle won")
                is_race_on = False
            random_number = randint(0, 55)
            turtle.forward(random_number)


screen.exitonclick()
