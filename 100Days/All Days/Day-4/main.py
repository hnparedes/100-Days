import random

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

choice_images = [rock, paper, scissors]

player_choice = int(input("Let's play Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
print(choice_images[player_choice])

cpu_choice = random.randint(0, 2)
print(choice_images[cpu_choice])

if player_choice >= 3 or player_choice < 0:
    print("You didn't follow the instructions, you lose.")
elif player_choice == 0 and cpu_choice == 2:
    print("You Win!!")
elif cpu_choice == 0 and player_choice == 2:
    print("You Lose.")
elif cpu_choice > player_choice:
    print("You Lose.")
elif player_choice > cpu_choice:
    print("You Win!!")
elif cpu_choice == player_choice:
    print("It's A Draw.")
