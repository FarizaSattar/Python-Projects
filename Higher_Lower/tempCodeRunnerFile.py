# Higher Lower
''' This code allows the user to play a game where they need to guess which Instagram account has more followers. '''

import os
from game_data import data
import random
from art import logo, vs


# This function will clear the console
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')  


# This function gives us a random Instagram account
def get_random_account():
  random_account = random.choice(data)
  return random_account


# This function formats the data of both Instagram accounts
def format_data(input_account):
  # Obtain values from keys
  name_in_account = input_account["name"]
  description_in_account = input_account["description"]
  country_in_account = input_account["country"]
  return f'{name_in_account}, a {description_in_account} from {country_in_account}'


# This function checks the user's answer
def check_answer(input_guess, input_1_followers, input_2_followers):
  if input_1_followers > input_2_followers:
    return input_guess == "1"
  else:
    return input_guess == "2"


# This function is where the game will be played
def play_game():

  # Print logo
  print(logo)

  # Start the user's score at 0
  user_score = 0

  # This variable will determine when the game ends
  should_game_continue = True

  # Obtain 2 random accounts
  account_1 = get_random_account()
  account_2 = get_random_account()

  # This code will keep on running until the user loses
  while should_game_continue:
    # Account 1 will be replaced by account 2
    account_1 = account_2
    # Account 2 will be replaced by a new random account
    account_2 = get_random_account()

    # If the new account 2 is equal to account 1, we will create a new account for account 2
    while account_1 == account_2:
      account_2 = get_random_account()

    # Both Instagram accounts will appear on the console
    print(f"Compare 1: {format_data(account_1)}")
    print(vs)
    print(f"Compare 2: {format_data(account_2)}")

    # Ask the user to choose either account 1 or account 2
    print()
    user_guess = input("Who has more followers? Type '1' or '2':\n")
    # Obtain values from keys to get follower count
    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]
    is_user_correct = check_answer(user_guess, follower_count_1,
                                   follower_count_2)

    # Clear screen for next round
    clear_screen()

    # Print logo to console
    print(logo)

    # If the user got the answer correct
    if is_user_correct:
      user_score += 1
      clear_screen()
      print(f"You got it correct! Current score: {user_score}")

    # If the user got the answer wrong
    else:
      should_game_continue = False
      clear_screen()
      print(f"You got it wrong! Final score: {user_score} ")

# Start the Higher Lower game
play_game()

play_another_round = input("Would you like to play again? Please type 'y' for yes and 'n' for no. ").lower()

if play_another_round == 'y':
    play_game()
        
else:
    clear_screen()
    print("Goodbye! Thank you for playing Higher Lower!")
