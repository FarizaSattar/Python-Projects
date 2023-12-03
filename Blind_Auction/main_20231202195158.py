# Blind Auction

''' The code collects bids from users, determines the highest bidder, and clears the console screen for an 
interactive bidding system. '''

# A function to clear the console screen (for Visual Studio Code, etc.)
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')  # Uses os.system to clear the console screen based on the operating system

from art import logo  # Imports the logo from the 'art' module
print(logo)  # Prints the logo at the beginning of the program

bids = {}  # Initializes an empty dictionary to store user bids
bidding_finished = False  # Initializes a flag to control the bidding process

def find_highest_bidder(bidding_record):
    # Function to determine the highest bidder and their bid amount
    highest_bid = 0  # Initializes the highest bid to 0
    winner = ""  # Initializes the winner's name as an empty string

    # Iterates through each bidder in the bidding record to find the highest bid and the corresponding bidder
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:  # Compares the bid amount to the current highest bid
            highest_bid = bid_amount  # Updates the highest bid if a higher bid is found
            winner = bidder  # Updates the winner's name corresponding to the highest bid

    print(f"The winner is {winner} with a bid of ${highest_bid}")  # Displays the winner and their bid amount

while not bidding_finished:
    name = input("What is your name?: ")  # Asks the user for their name
    price = int(input("What is your bid?: $"))  # Asks the user for their bid amount
    bids[name] = price  # Stores the user's bid in the 'bids' dictionary using their name as the key

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")  # Asks if there are more bidders
    if should_continue == "no":
        bidding_finished = True  # Ends the bidding process if there are no more bidders
        find_highest_bidder(bids)  # Calls the function to determine the highest bidder and display the result
    elif should_continue == "yes":
        clear_screen()  # Clears the console screen if there are more bidders to start a new bid entry
