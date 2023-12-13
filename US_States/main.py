# US States

''' The code allows the user to play a guessing game for U.S. states. '''

import turtle  
import pandas  

# Create a screen and set its title for the U.S. States Game
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the map image and set it as the background shape of the turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data containing U.S. states from a CSV file
data = pandas.read_csv("50_states.csv")

# Convert the states from the data into a list
all_states = data.state.to_list()

# List to store guessed states by the user
guessed_states = []

# Continuously prompt the user to guess state names until all states are guessed or the user chooses to exit
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()  # Prompt user for state name input

    # If the user chooses to exit, create a list of states not guessed and save it to a CSV file
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the guessed state is in the list of U.S. states
    if answer_state in all_states:
        guessed_states.append(answer_state)  # Add the correctly guessed state to the list

        # Create a turtle to mark the guessed state's location on the map
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle icon
        t.penup()  # Lift the pen to avoid drawing lines when moving
        state_data = data[data.state == answer_state]  # Retrieve data of the guessed state from the dataset
        t.goto(int(state_data.x), int(state_data.y))  # Move the turtle to the state's coordinates on the map
        t.write(answer_state)  # Display the name of the guessed state on the map
