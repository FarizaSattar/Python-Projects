from turtle import Turtle

FONT = ("Courier", 24, "normal")  # Font style for displaying text

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the starting level
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.goto(-280, 250)  # Position the scoreboard
        self.update_scoreboard()  # Update the scoreboard to display the initial level

    def update_scoreboard(self):
        # Clear previous text and display the current level
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Increase the level and update the scoreboard
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display "GAME OVER" at the center of the screen
        self.goto(0, 0)  # Position the cursor to the center
        self.write(f"GAME OVER", align="center", font=FONT)  # Display the game over message
