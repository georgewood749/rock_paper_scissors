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

#Write your code below this line 👇

choices = [rock, paper, scissors]

# random.seed(input("Please enter a seed number for the RNG:\n"))

player_entry = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_entry < 0 or player_entry >=3:
  print("You entered an invalid number. Try again.")
else:

  player_choice = choices[player_entry]

  randomise = random.randint(0, 2)

  ai_choice = choices[randomise]

  print(f"\nYou played:\n{player_choice}")
  print(f"\nAI played:\n{ai_choice}")


  if player_entry == 0 and (randomise == 1):
    print("You lose!")
  if player_entry == 1 and randomise == 2:
    print("You lose!")
  if player_entry == 2 and randomise == 0:
    print("You lose!")

  if (player_entry == 1) and (randomise == 0):
    print("You win!")
  if (player_entry == 2) and (randomise == 1):
    print("You win!")
  if (player_entry == 0) and (randomise == 2):
    print("You win!")

  if (player_entry == 0) and (randomise == 0):
    print("You drew.")
  if (player_entry == 1) and (randomise == 1):
    print("You drew.")
  if (player_entry == 2) and (randomise == 2):
    print("You drew.")

