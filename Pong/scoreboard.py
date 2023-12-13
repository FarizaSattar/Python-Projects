from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Set the text color of the scoreboard to white
        self.color("white")  
        # Lift the pen to avoid drawing when moving
        self.penup() 
        # Hide the turtle icon
        self.hideturtle()  
        # Initialize the left player's score to 0
        self.l_score = 0  
        # Initialize the right player's score to 0
        self.r_score = 0  
        # Update the scoreboard to display the initial scores
        self.update_scoreboard()  

    def update_scoreboard(self):
        # Clear previous score display
        self.clear()  
        # Position the turtle to display the left player's score
        self.goto(-100, 200)  
        # Display the left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  
        # Position the turtle to display the right player's score
        self.goto(100, 200)  
        # Display the right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  

    def l_point(self):
        # Increment the left player's score by 1
        self.l_score += 1  
        # Update the scoreboard to reflect the score change
        self.update_scoreboard()  

    def r_point(self):
        # Increment the right player's score by 1
        self.r_score += 1  
        # Update the scoreboard to reflect the score change
        self.update_scoreboard()  
