# Turtle Race
''' The code creates a turtle race game where the user selects 1 out of 6 turtles to bet on. '''

from turtle import Turtle, Screen
import random

# Set up initial variables and screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Please make your bet",
    prompt="Which turtle will win the race? Please enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles 
for turtle_index in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(colors[turtle_index])
  new_turtle.goto(x=-230, y=y_positions[turtle_index])
  all_turtles.append(new_turtle)

# Start the race when a user makes a bet
if user_bet:
  is_race_on = True

# Check when turtle crosses the finish line and determine winner
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()

      # Print results of the turtle race
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")

    # Each turtle will move a random distance forward
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

# Close the window
screen.exitonclick()
