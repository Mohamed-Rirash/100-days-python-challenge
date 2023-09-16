#importing modules
import random
from art import logo,vs 
from game_data import data
import os

def format_data(acount):
    '''Format account data into printable format.'''
     
    name = acount["name"]    
    discription = acount["description"]
    country = acount["country"]
    return f"a {name} a {discription} from {country}"


def check_answer(guess,a_flower,b_flower):
    """check if the user_guess is correct"""
    if a_flower > b_flower:
        return guess == "a"
    else:
        return guess == "b"








# display arts
print(logo)
score = 0
is_continue = True
b = random.choice(data)

# Make game repeatable.
while is_continue:
#Generate a random account from the game data.
    a = random.choice(data)
    a = b
    b = random.choice(data)

    while a == b:
        b = random.choice(data)
        
        
    #call the functon
    print(f"compare A: {format_data(a)}")
    print(vs)
    print(f"compare B: {format_data(b)}")


    # Ask user for a guess.
    user_guess  = input("who has more flowes A or B: ").lower()


    # Check if user is correct.
    ## Get follower count.
    a_follower = a["follower_count"]
    b_follower = b["follower_count"]

    is_correct = check_answer(guess=user_guess,a_flower=a_follower,b_flower=b_follower)
    os.system("clear")
    print(logo)
    # Feedback.
    if is_correct:
    # Score Keeping.
        score += 1
        print(f"your are right ! current score: {score}")
    else:
        is_continue = False
        print(f"sorry! that is wrong your finel score: {score}")


