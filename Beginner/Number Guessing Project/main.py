""" sometimes it's just best to leave variables in global/larger
scope and keep functions together with helper methods; definitely could
have broken down the guess method where one thing checks and returns
turns

biggest thing was the while loop condition - could do

while guess != answer:
"""
import random

EASY_GUESS = 10
HARD_GUESS = 5

#don't need function but helps with readability
def intro():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    return random.randint(1,100)


def choose_diff():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return HARD_GUESS
    elif difficulty == "easy":
        return EASY_GUESS

def guess(rand, guesses):
    user_guess = int(input("Make a guess: "))
    #if else statements in different function
    if user_guess == rand:
        print("You got the number correct!")
        return True
    elif user_guess > rand:
        print("Too high. \nGuess again.") #guess again will show up even if they have 0 guesses left
    else:
        print("Too low. \nGuess again.")
    guesses-=1
    print(f"You have {guesses} attempts remaining to guess the number.")
    if guesses == 0:
        print("Sorry, you have run out of guesses.")
        return True, guesses
    else:
        return False, guesses

random_num = intro()
guesses = choose_diff()
print(f"you have {guesses} attempts remaining to guess the number.")
correct_guess = False
while not correct_guess:
    correct_guess, guesses = guess(random_num, guesses)