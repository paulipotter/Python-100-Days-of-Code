
# source: https://www.geeksforgeeks.org/clear-screen-python/
import os
from subprocess import call
from art import *

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')
    
def get_winner(bidders):
    winner_amt = 0
    winner_name = ''
    for key in bidders:
        if bidders[key] > winner_amt:
            winner_amt = bidders[key]
            winner_name = key
    print(f'The winner is {winner_name} with ${winner_amt}')
    
more_bidders = True
bidders = {}
while more_bidders:
    bidder_name = input("What is your name? ")
    bidder_bid = int(input("What is your bid? "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    bidders[bidder_name] = bidder_bid
    
    if other_bidders == 'yes':
        continue
    else:
        get_winner(bidders)
    