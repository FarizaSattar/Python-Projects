# Blind Auction
''' Ths code allows the user to hold a blind auction '''

from art import logo

# Clear screen after each bid
def clear_screen():
  import os
  os.system('cls' if os.name == 'nt' else 'clear')

# Create dictionary to store the bids and bidders
bids = {}
bidding_is_finished = False

# This function will calculate the highest bid and its corresponding bidder
def calculate_highest_bidder(bidding_info):

# Create variable to record highest bid and string to record the corresponding bidder's name
  highest_bid = 0
  winner = ""

# Loop through all bidders and compare them with each other until we get the highest bidder
  for current_bidder in bidding_info:
    current_user_bid = bidding_info[current_bidder]
    if current_user_bid > highest_bid:
      highest_bid = current_user_bid
      winner = current_bidder

# The result of the blind auction
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# This section of the code allows users to keep on inputting bids 
while not bidding_is_finished:
    
# The user will input their name and bid
  user_name = input("What is your name?: ")
  user_price = int(input("What is your bid?: $\n"))
  bids[user_name] = user_price
  
# This section of the code asks the user is there is anyone else who wants to make a bid
should_bid_continue = input("Is there anyone else who wants to make a bid? Please type 'yes' or 'no'\n")

# If there is no one left, the highest bidder will be calculated
if should_bid_continue == "no":
    bidding_is_finished == True
    calculate_highest_bidder(bids)
    
# If there is a user who needs to make a bid, the screen will clear
elif should_bid_continue == "yes":
    clear_screen()