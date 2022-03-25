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
    
def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    return sum(card_list)

def dealer_wins():
    print('Dealer wins! You lose :(')

def user_wins():
    print('You win! Congrats!')

def draw():
    print("It's a draw!")
  
keep_playing = True
while keep_playing:  
    user_cards = [deal_card()]
    dealer_cards = [deal_card()]

    keep_going = True
    while(keep_going):
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        
        print(logo)
        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if ace_plus_ten(user_cards):
            user_wins()
            
        elif ace_plus_ten(dealer_cards):
            print(f"Computer has {dealer_cards}")
            dealer_wins()
            

        if user_score > 21:
            if 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                if calculate_score(user_cards) > 21:
                    dealer_wins()
                    
                else: 
                    print(f"Your cards: {user_cards}, your score: {user_score}")
            else:
                dealer_wins()
                
                    
        more_cards = input('Would you like to get another card? y/n: ').lower()

        if more_cards == 'y':
            continue
        else:
            keep_going = False
            
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

    if dealer_score > 21:
        user_wins()
        
    else:
        if user_score > dealer_score:
            user_wins()
        elif user_score < dealer_score:
            dealer_wins()
        else:
            draw()
    
    keep_playing = input('Would you like to play again? y/n: ').lower()

    if keep_playing == 'y':
        clear()
    else:
        keep_playing = False
        