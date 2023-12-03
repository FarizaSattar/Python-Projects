from turtle import Turtle

# Constants for player's starting position, movement distance, and finish line
STARTING_POSITION = (0, -280)  # Player's starting position
MOVE_DISTANCE = 10  # Distance to move the player
FINISH_LINE_Y = 280  # Y-coordinate for the finish line

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the shape of the player as a turtle
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.go_to_start()  # Set the player to the starting position
        self.setheading(90)  # Set the player's orientation to face upwards

    def go_up(self):
        # Move the player forward (upwards) by MOVE_DISTANCE units
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move the player to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has reached the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True  # Return True if the player's y-coordinate is beyond the finish line
        else:
            return False  # Return False if the player hasn't reached the finish line
