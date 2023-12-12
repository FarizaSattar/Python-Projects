# Blackjack
''' The code will allow the user to play a game of Blackjack with the computer. '''

import os
import random
from art import logo


# This function will clear the console
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')  


# This function deals a single random card
def deal_random_card():
  # This is the deck of cards. By default the ace will be worth 11 points unless the user's score is greater than 21
  card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(card_deck)
  return random_card


# This function will return the user's score for their deck of cards
def calculate_score(input_cards):

  # Check for situation where user has an ace and a 10. The ace will be worth 11 points
  if sum(input_cards) == 21 and len(input_cards) == 2:
    # 0 means that you have a Blackjack
    return 0

  # Check for situation where user has an ace. It will be worth 1 point if the total score is greater than 21
  if 11 in input_cards and sum(input_cards) > 21:
    # Remove the item 11 in the user's card deck and replace with 1
    input_cards.remove(11)
    input_cards.append(1)

  # If user has no aces
  return sum(input_cards)


# This function will compare the user's and computer's scores to find the winner
def compare_final_scores(user_score, computer_score):

  # The user and computer both have a score greater than 21
  if user_score > 21 and computer_score > 21:
    return "You both lose! You both went over 21 points!"

  # The user and computer have the same score
  elif user_score == computer_score:
    return "You have a draw!"

  # The user has a Blackjack
  elif user_score == 0:
    return "Congrats! You win! You have a Blackjack!"

  # The computer has a Blackjack
  elif computer_score == 0:
    return "You lose! The computer has a Blackjack!"

  # The user has a score greater than 21
  elif user_score > 21:
    return "You lose!"

  # The computer has a score greater than 21
  elif computer_score > 21:
    return "You lose!"

  # The user has a greater score than the computer
  elif user_score > computer_score and user_score < 21:
    return "Congrats! You win! "

  # The user has a higher score than the computer and less than 21
  elif user_score < computer_score and user_score < 21:
    return "You lose!"

  # The user has a score less than 21 and the computer has a score greater than 21
  elif user_score < 21 and computer_score > 21:
    return "Congrats! You win!"

  # The user will lose
  else:
    return "You lose!"


# This function handles the game function
def play_blackjack():

  # Print logo to console
  print(logo)

  # Create deck of cards for user and computer
  user_cards = []
  computer_cards = []

  # Winning conditions
  is_blackjack_over = False

  # Give the user and computer 2 cards to start with
  for _ in range(2):
    user_cards.append(deal_random_card())
    computer_cards.append(deal_random_card())

  # Run code until game ending conditions are met
  while not is_blackjack_over:
    # Calculate score for both user and computer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    # Print results to console and add an empty line to improve readability
    print()
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # End game if anyone gets a Blackjack or scores more than 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_blackjack_over = True

    else:
      # Print empty line to console to improve readability
      print()

      # Ask user if they want to read another card
      ask_user_deal = input("Type 'y' to get another card. Type 'n' to pass\n")

      # If the user says yes to dealing another card
      if ask_user_deal == "y":
        user_cards.append(deal_random_card())

      # If the user says no to dealing another card
      else:
        is_blackjack_over = True

    # The computer will keep on dealing cards as long as its score is between 0 and 16
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_random_card())
      computer_score = calculate_score(computer_cards)

    if is_blackjack_over is True:
      # Print empty line to console to improve readability
      print()
      print(f"Your final hand: {user_cards}, final score: {user_score}")
      print(
          f"Computer's final hand: {computer_cards}, final score: {computer_score}"
      )
      print(compare_final_scores(user_score, computer_score))

      # Print empty line to console to improve readability
      print()

      # Ask the user if they want to play another round of Blackjack
      play_another_round = input(
          "Do you want to play another game of Blackjack? Type 'y' for yes and 'n' for no\n"
      ).lower()

      # Clear screen
      clear_screen()

      # If the user says yes to playing another round of Blackjack
      if play_another_round == "y":
        play_blackjack()

      # If the user says no to playing another round of Blackjack
      else:
        print("Goodbye! Thank you for playing Blackjack!")


play_blackjack()
