from random import randint
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, number, attempts_left):
    if user_guess > number:
        print("Too high.\nGuess again.")
        return attempts_left - 1
    elif user_guess  < number:
        print("Too low.\nGuess again.")
        return attempts_left - 1
    else: #guess is correct
        print(f"You guessed it! The answer is {number}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # if easy then 100, else if hard then 5
    if difficulty == 'easy':
        return EASY_LEVEL
    elif difficulty == 'hard':
        return HARD_LEVEL

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")

    # number of turns depends on difficulty chosen
    attempts_left = set_difficulty()
        
    # generate number
    number = randint(1,100)
    user_guess = 0
    while user_guess != number:
        print(f"\n\nYou have {attempts_left} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts_left = check_answer(user_guess, number, attempts_left)
        if attempts_left == 0:
            print("You're out of guesses. Game Over.")
            
game()
    