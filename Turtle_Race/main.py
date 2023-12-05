# Turtle Race

''' The code creates a turtle race game where the user selects a turtle color to bet on and then simulates a 
race among six turtles, announcing the winner or loser based on the user's chosen color and the turtle that 
reaches the finish line first. '''

from turtle import Turtle, Screen  # Import required modules
import random  # Import random module

is_race_on = False  # Initialize a flag to control the race
screen = Screen()  # Create a screen for the race
screen.setup(width=500, height=400)  # Set up the screen dimensions
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # Get user's bet
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of turtle colors
y_positions = [-70, -40, -10, 20, 50, 80]  # Y-axis starting positions for turtles
all_turtles = []  # List to hold all turtle objects

# Create 6 turtles, set their initial properties and positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)  # Add turtles to the list

if user_bet:  # If the user makes a bet, start the race
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # Stop the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")  # Announce the winner
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")  # Announce the loser

        # Make each turtle move a random distance forward
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)  # Move the turtle forward by the random distance

screen.exitonclick()  # Close the window when clicked
