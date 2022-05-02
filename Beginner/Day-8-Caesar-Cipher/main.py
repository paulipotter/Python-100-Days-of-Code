from pydoc import plain
from art import logo
direction, text, shift = "","",""
restart = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_txt, shift_amt, cipher_direction):
    new_text = ""
    if direction == 'decode':
            shift_amt *= -1
    for letter in start_txt:
        if not letter.isalpha():
            new_text += letter
        else:
            new_position = alphabet.index(letter) + shift_amt
            new_text += alphabet[new_position]
    print(f"The {direction}d text is {new_text}")
    
print(logo)

while(restart):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction != 'encode' and direction != 'decode':
        print('Incorrect input. Please try again')
        continue
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: ")) % 26
        
    caesar(text, shift, direction)
    
    restart_prompt = input("Would you like to restart the program? Type Y/N: ").lower()
    if restart_prompt == "n":
        restart = False
    