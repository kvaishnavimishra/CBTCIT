import random

rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''
game_images = [rock, paper, scissors]

while True:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

  if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")

  play_again = input("Do you want to play again? Type 'yes' to continue or 'no' to quit.\n").lower()
  if play_again != 'yes':
    break

print("Thanks for playing!")
