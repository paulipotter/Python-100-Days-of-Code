# TO DO - input validation!!!!
from random import choice
from hangman_art import logo, stages
from hangman_words import word_list

hangman_word = []
chosen_word = choice(word_list)
game_over = False
lives = 6

# Create the display
for i in range(len(chosen_word)):
  hangman_word.append("_")

print(f"The word is {chosen_word}")


while not game_over:
    
    # Ask for user input
    print(logo)
    guess = input("Guess a letter: ").lower()

    # Check if user is wrong
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            print("You Lost!")
            print(f"word was {chosen_word}")
            game_over = True
      
    # Check guessed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            hangman_word[position] = guess
    
    # Print progress
    print(stages[lives])        
    print(*hangman_word)

    # Check if won
    if "_" not in hangman_word:
        print("You won!")
        game_over = True
