# Guess Number

''' The code implements a number guessing game where the user guesses a randomly generated number within a 
specific range, using a defined number of turns based on the selected difficulty level, and provides hints to 
help the user guess the correct number within the allowed attempts. '''

from random import randint  # Importing randint function from the 'random' module
from art import logo  # Importing the logo from the 'art' module

EASY_LEVEL_TURNS = 10  # Setting the number of turns for easy level
HARD_LEVEL_TURNS = 5   # Setting the number of turns for hard level

# Function to check user's guess against the actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:  # If the guess is higher than the answer
        print("Too high.")
        return turns - 1  # Decrease the number of turns by 1
    elif guess < answer:  # If the guess is lower than the answer
        print("Too low.")
        return turns - 1  # Decrease the number of turns by 1
    else:  # If the guess is correct
        print(f"You got it! The answer was {answer}.")

# Function to set difficulty level.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":  # If the user chooses easy difficulty
        return EASY_LEVEL_TURNS  # Return the number of turns for easy level
    else:  # If the user chooses hard difficulty
        return HARD_LEVEL_TURNS  # Return the number of turns for hard level

def game():
    print(logo)  # Display the game logo
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)  # Randomly generate the answer between 1 and 100
    print(f"Pssst, the correct answer is {answer}")  # Display the correct answer (for testing purposes)

    turns = set_difficulty()  # Set the number of turns based on user-selected difficulty

    guess = 0  # Initialize guess to 0
    while guess != answer:  # Loop until the user's guess matches the answer
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if the guess is incorrect
        turns = check_answer(guess, answer, turns)
        if turns == 0:  # If the turns reach 0
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:  # If the guess is incorrect but attempts are remaining
            print("Guess again.")

game()  # Start the game
