# Blackjack

''' The code implements a Blackjack game in Python, allowing users to play against the computer, utilizing 
functions to deal cards, calculate scores, compare them, and offering an option to restart the game after 
completion. '''

# Import necessary libraries and functions
import random  # For generating random cards
from replit import clear  # For clearing the console
from art import logo  # For displaying the game logo

# Function to deal a random card from the deck
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Deck of cards
  card = random.choice(cards)  # Choose a random card
  return card

# Function to calculate the total score from a list of cards
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  # Check for a blackjack (ace + 10) and return 0 instead of the actual score
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # Check for an ace (11) and adjust the score if it exceeds 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# Function to compare user and computer scores and determine the winner
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

# Function to handle the game logic
def play_game():
  print(logo)  # Display the game logo

  # Deal 2 cards each to the user and the computer
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    # Check if the game ends based on user/computer blackjack or score exceeding 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Let the computer play based on defined rules
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # Display final hands and determine the winner
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

# Ask the user if they want to restart the game and handle game restart
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()  # Clear the console
  play_game()  # Start the game
