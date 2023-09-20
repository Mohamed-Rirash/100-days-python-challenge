import random
import os
from art import logo

print(logo)
def deal_card():
    """this function return random cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
    
def compare(user_score ,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose opponent has BlackJack"
    elif user_score == 0:
        return "win with Black Jack"
    elif user_score > 21:
        return "you went over. You lose"
    elif computer_score > 21:
        return "opponent went over! You Win"
    elif user_score > computer_score:
        return
    else:
        return "computer won"

def playGame():
    userCards = []
    computerCards = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        userCards.append(deal_card())
        computerCards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(userCards)
        computer_score = calculate_score(computerCards)
        print(f"Your card {userCards} current score {user_score}")
        print(f"computer`s firs card {computerCards[0]}")
        
        if user_score == 0 or calculate_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card or 'n' to pass: ").lower()
            print(f"Your card {userCards} your score {user_score}")
            print(f"computer cards {computerCards} computer score {computer_score}")
            if user_should_deal == "y":
                userCards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computerCards.append(deal_card())
        computer_score = calculate_score(computerCards)
        
    print(f"Your final hand: {userCards} final score: {user_score}")
    print(f"computer final hand: {computer_score} final score: {computer_score}")

    print(compare(user_score,computer_score))

while input("Do you want to play agame 'y' or 'n' :").lower() == "y":
    os.system('clear')
    playGame()