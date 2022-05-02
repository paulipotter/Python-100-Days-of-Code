hand_gestures = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']


import random
user_play = int(input("0 - Rock\n1 - Paper\n2 - Scissors\nWhat do you choose? "))
print(hand_gestures[user_play])

computer_play = random.randint(0,2)
print(f"Computer chose {computer_play}")
print(hand_gestures[computer_play])

if user_play == computer_play:
    print("Draw!")
elif user_play == 0 and computer_play == 2:
    print("User wins!")
elif computer_play == 0 and user_play == 2:
    print("Computer wins!")
elif computer_play > user_play:
    print("Computer wins!")
else:
    print("User wins!")