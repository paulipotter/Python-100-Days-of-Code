from random import randint

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# if easy then 100, else if hard then 5
if difficulty == 'easy':
    attempts_left = 10
elif difficulty == 'hard':
    attempts_left = 5
    
guessed = False
# generate number
number = randint(1,100)
while attempts_left > 0 and not guessed:
    print(f"\n\nnumber is {number}")
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess > number:
        print("Too high.\nGuess again.")
        attempts_left -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts_left -= 1
    else: #guess is correct
        print(f"You guessed it! The answer is {number}")
        guessed = True
        
        
        

