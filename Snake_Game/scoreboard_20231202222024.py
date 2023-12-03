from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position the scoreboard
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score and update the scoreboard."""
        self.score += 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update the scoreboard with the new score
