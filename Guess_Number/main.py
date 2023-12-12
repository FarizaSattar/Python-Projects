# Guess Number
''' The code will allow the user to play a number guessing game with the computer. '''

import os
from random import randint
from art import logo

# The number of turns for each difficulty level
TURNS_FOR_EASY_LEVEL = 10
TURNS_FOR_HARD_LEVEL = 5
number_of_turns = 0

# This function will clear the console
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')  

# This function will determine the number of turns that the user will have
def set_difficulty_level():
  difficulty_level = input(
      "Please choose a difficulty level. Type in 'e' for easy or 'h' for hard\n"
  ).lower()

  if difficulty_level == "e":
    return TURNS_FOR_EASY_LEVEL
  else:
    return TURNS_FOR_HARD_LEVEL

# This function will check the user's guess against the random number, and decrease the number of turns if they get it wrong
def check_user_guess(user_guess, number_to_guess):

  # If user guesses a number that is too high
  if user_guess > number_to_guess:
    # Print a blank link to improve readability
    print()
    print("The number is too high!")
    return False

  # If the user guesses a number that is too low
  elif user_guess < number_to_guess:
    # Print a blank link to improve readability
    print()
    print("The number is too low!")
    return False

  # If the user guesses the correct number
  else:
    clear_screen()
    # Print a blank link to improve readability
    return True

# This function will run the guessing game
def play_guessing_game():

  # Welcome Message
  print(logo)
  print('Welcome to the guessing game!')
  print("I am thinking of a number between 1 and 100.")
  random_number = randint(1, 100)

  # Initalize the number of turns that the user has and their attempts
  number_of_turns = set_difficulty_level()
  user_guess = 0

  # Allow the user to make a guess and end the game if they run out of guesses
  while user_guess != random_number:

    # Print a blank link to improve readability
    print()

    # List the user's remaining lives
    print(f"You have {number_of_turns} attempts!")

    # Allow the user to guess a number
    user_guess = int(input("Please make a guess:\n"))
    check_user_guess(user_guess, random_number)
    number_of_turns -= 1

    if user_guess == random_number:
      print()
      print(f"Congrats! You win! The answer was {random_number}")

    # If the user runs out of guesses
    elif number_of_turns == 0:
      # Print a blank link to improve readability
      print()
      print(
          f"You lose! You ran out of guesses! The number was {random_number}")
      return

    # If the user guesses the wrong number but has remaining turns
    else:
      # Print a blank link to improve readability
      print()
      print("Please guess again!")

play_guessing_game()
