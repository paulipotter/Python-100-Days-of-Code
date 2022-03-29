from game_data import data
from art import logo, vs
from random import choice
import os
from subprocess import call

def clear():
    # Clear function - source: https://www.geeksforgeeks.org/clear-screen-python/
    _ = call('clear' if os.name =='posix' else 'cls')
    
def get_random_account():
    return choice(data)

def formatted_sentence(option):
    return f"{option['name']}, a(n) {option['description']}, from {option['country']}."

def compare_followers(a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return 'a'
    elif a_follower_count > b_follower_count:
        return 'b'
    else:
        return 'draw'
    
def check_answer(a_follower_count, b_follower_count, guess):
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    result = True
    score = 0
    option_a = get_random_account()
    print(logo)
    
    while result:
        if score > 0:
            print(f"You're right! Current score: {score}")
        
        option_b = get_random_account()
        
        print(f"Compare A: {formatted_sentence(option_a)}", option_a['follower_count'])
        print(vs)
        print(f"Compare B: {formatted_sentence(option_b)}", option_b['follower_count'])
        user_choice = input("Who do you think has more followers? Please type 'A' or 'B': ").lower()

        result = check_answer(option_a['follower_count'], option_b['follower_count'], user_choice)
        
        if result:
            score +=1
            option_a = option_b    
        clear()
        print(logo)
    print(f"You're wrong! Final score: {score}")
            
    
game()