import os  # Import the 'os' module for console clearing
import random
from art import logo  # Importing the game's logo from the 'art' module

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for Blackjack (Ace + 10) and return 0 for a Blackjack hand
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for an Ace (11) and adjust its value to 1 if the total score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    # Determine the game outcome based on scores and specific conditions
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

def play_game():
    print(logo)  # Display the game logo at the start of each game session

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial 2 cards to the player and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Calculate scores and check if game conditions for ending are met
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Prompt user to draw another card or pass
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Add another card to the player's hand
            else:
                is_game_over = True

    # Computer's turn to draw cards based on set rules
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final hands and scores, then determine the game's result
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Start the game based on user input to play another round
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console
    play_game()  # Initiate a new game session
