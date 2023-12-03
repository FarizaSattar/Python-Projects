# Turtle Crossing

''' The code implements a "Turtle Crossing" game where a player navigates through moving cars, accumulating 
points for successful crossings while ending the game upon collision with a car. '''

# Import necessary modules and classes
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create instances of Player, CarManager, and Scoreboard
player = Player()  # Create the player object
car_manager = CarManager()  # Create the car manager object
scoreboard = Scoreboard()  # Create the scoreboard object

# Listen for user input (up arrow key) to move the player up
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True  # Flag to control the game loop
while game_is_on:
    time.sleep(0.1)  # Introduce a small delay for smoother gameplay
    screen.update()  # Update the screen manually

    car_manager.create_car()  # Create a new car
    car_manager.move_cars()  # Move all cars created

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check if the player collides with any car
            game_is_on = False  # End the game if there's a collision
            scoreboard.game_over()  # Display "Game Over" on the scoreboard

    # Detect successful crossing to the finish line
    if player.is_at_finish_line():  # Check if the player reaches the finish line
        player.go_to_start()  # Reset the player's position to the starting point
        car_manager.level_up()  # Increase car speed as the player crosses successfully
        scoreboard.increase_level()  # Increase the level on the scoreboard

# Exit the game when the screen is clicked
screen.exitonclick()
