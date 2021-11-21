rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# Rock beats Scissors, Paper beats Rock, Scissors beat Paper
# 0 for Rock
# 1 for Paper
# 2 for Scissors

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice < 0:
  print("Invalid choice, you lose.")
else:
  print(game_images[player_choice])

  computer_choice = random.randint(0, 2)
  print("The computer chooses: ")
  print(game_images[computer_choice])


  if player_choice == 0 and computer_choice == 2:
    print("You win!")
  elif player_choice == 2 and computer_choice == 0:
    print("You lose")
  elif player_choice > computer_choice:
    print("You win!")
  elif computer_choice > player_choice:
    print("You lose")
  elif player_choice == computer_choice:
    print("It's a draw")
