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

''' 
tasks - creating list of rock paper scissors and choosing a random one for computer
get user input and assign choice
compare choice
'''
#computer choice
options = [rock, paper, scissors]
computer_choice = random.choice(options)
#user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
if user_choice == 0:
    user_choice = rock
elif user_choice == 1:
    user_choice = paper
elif user_choice == 2:
    user_choice = scissors
else:
    print("Choose one of the options")
    exit()
#compare
print(f" {user_choice}")
print(f"Computer chose: \n {computer_choice}")
if user_choice == computer_choice:
    print("Draw")
elif user_choice == rock and computer_choice == scissors:
    print("You win")
elif user_choice == paper and computer_choice == rock:
    print("You win")
elif user_choice == scissors and computer_choice == paper:
    print("You win")
else:
    print("You lose")

'''
another solution was to create a list and use the index to print the image 
(e.x. - 
images = [rock, paper, scissors]
print(images[user_choice]) or computer choice
focus more on number than variable comparison
import random

user_choice=int(input("Pick 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice > 2 or user_choice < 0:
    print("Choose a valid number")
    exit()

computer_choice = random.randint(0,2)
images = [rock, paper, scissors]

print(images[user_choice])
print(f"Computer chose: \n{images[computer_choice]}")

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
else: 
    print("You lose")
'''