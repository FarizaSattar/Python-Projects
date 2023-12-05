from turtle import Turtle
import random

# List of colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Constants defining starting and incrementing move distances for cars
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []  # List to store all car instances created
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of the cars

    def create_car(self):
        # Create cars randomly with a 1 in 6 chance
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new car instance
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Set the car's shape
            new_car.penup()  # Lift the pen to avoid drawing when moving
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-250, 250)  # Randomly position the car on the y-axis
            new_car.goto(300, random_y)  # Set the initial position of the car off-screen
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move_cars(self):
        # Move all cars in the car list towards the left side of the screen
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move the car backwards based on its speed

    def level_up(self):
        # Increase the speed of the cars as the game level increases
        self.car_speed += MOVE_INCREMENT  # Increment the speed of the cars
