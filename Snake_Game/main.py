# Snake Game

''' The code allows the user to play the Snake game. '''

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turns off automatic screen updates
screen.tracer(0)  

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keypress events to control the snake's movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game loop
game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()  
    # Pause to control game speed
    time.sleep(0.1)  
    # Move the snake
    snake.move()  

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Keep the window open until the user clicks to exit
screen.exitonclick()
