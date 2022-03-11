from ascii_art import *

print(treasure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

user_choice = ''


user_choice = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if user_choice == 'left':
    print(island)
    user_choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
else:
    print("You fell into a hole. Game Over.")

if user_choice == "wait":
    print(doors)
    user_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
else:
    print("You get attacked by an angry trout. Game Over.")

if user_choice == "yellow":
    print(fire_game_over)
    print("It's a room full of fire. Game Over.")
elif user_choice == "blue":
    print("You found the treasure! You Win!")
elif user_choice == "red":
    print(fire_game_over)
    print("You enter a room of beasts. Game Over.")
else:
    print(win)
    print("You chose a door that doesn't exist. Game Over.")
