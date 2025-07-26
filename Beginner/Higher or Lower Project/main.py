from art import logo
import random
from art import vs
from game_data import data

#for list of dictionaries you can use random.choice to get random dictionary
def random_person():
    person1 = random.choice(list(data))
    person2 = person2_random(person1)
    return person1, person2

def person2_random(person1):
    person2 = random.choice(list(data))
    while person1 == person2:
        person2 = random.choice(list(data))
    return person2

def compare(person1, person2):
    phrase1 = person1["name"] + ", a " + person1["description"] + ", from " + person1["country"] + "."
    phrase2 = person2["name"] + ", a " + person2["description"] + ", from " + person2["country"] + "."
    print(f"Compare A: {phrase1}")
    print(vs)
    print(f"Against B: {phrase2}")

def lose(score):
    for i in range (25):
        print()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def followers(person1, person2, score):
    response = input("Who has more followers? Type 'A' or 'B': ")
    if (response == "A" and person1["follower_count"]>=person2["follower_count"] or
            response == "B" and person2["follower_count"]>=person1["follower_count"]):
        score+=1
        print(f"You're right! Current score: {score}")
        if response == "A":
            person2 = person2_random(person1)
        else:
            person1 = person2
            person2 = person2_random(person1)
        return True, score, person1, person2
    else:
        lose(score)
        return False, score, person1, person2


print(logo)
score = 0
person1, person2 = random_person()
still_going = True
while still_going:
    #can update score within and use the followers method to see if their score is right or wrong
    #slight difference, I take the person with the most followers and continue, she takes in person whose last
    compare(person1, person2)
    still_going, score, person1, person2 = followers(person1, person2, score)

#start adding more code in main to reduce returning multiple parameters
#print stuff in main so you can avoid passing it in and returning it out again