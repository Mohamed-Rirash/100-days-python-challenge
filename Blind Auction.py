# Import the necessary modules
from art import logo
import os

# Display the welcome message
print(logo)
print("Welcome to the Blind Auction program".upper())

# Initialize variables
bidders = {}
add_another_one = ""

bidders = {}
add_another_one = "yes"

while add_another_one == "yes":
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What's your bid?: $"))
    bidders[bidder_name] = bidder_amount

    # Clear the console before asking for another bidder
    os.system('clear')

    add_another_one = input("Are there any other bidders? Type 'yes' or 'no': ").lower()


   
# Find the bidder with the highest bid
highest_bid = 0
winner = ""
for bider, bid in bidders.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = bider




# Display the winner
print(f"the winnner is {winner} with the amount of ${highest_bid}")
