from operator import truediv
from random import choice
import os
from subprocess import call
from art import *


def clear():
    # Clear function - source: https://www.geeksforgeeks.org/clear-screen-python/
    _ = call('clear' if os.name =='posix' else 'cls')
    
def deal_card():
    """Returns a random card from the deck."""
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def ace_plus_ten(cards):
    if 10 in cards and 11 in cards:
        return True
    else:
        return False
    
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # zero = blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)

def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        return "Your score is over 21. You lose!\n"
    if user_score == dealer_score:
        return "It's a draw!\n"
    elif user_score == 0:
        return "Win with a Day-11-Blackjack!\n"
    elif user_score > 21:
        return "Your score is over 21. You lose!\n"
    elif user_score > dealer_score:
        return "You win!\n"
    else: return "You lose!\n"

def blackjack():   
    #Init list and deal first card
    user_cards = [deal_card()]
    dealer_cards = [deal_card()]

    game_over = False
    while not game_over:
        #Deal second card and calculate score
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        
        #Print cards and console scores
        print(logo)
        print(f"\nYour cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}\n")

        #Check if any have a Day-11-Blackjack or if user already lost - If so, game over
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:        
            more_cards = input('Would you like to get another card? y/n: ').lower()
            if more_cards == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    #Dealer gets more cards until while loop breaks
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        
    #Print final game numbers
    print(f"\nYour final cards are {user_cards}, final score: {user_score}")
    print(f"The dealer's final cards are {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

        
while input("Would you like to play a game of Day-11-Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()