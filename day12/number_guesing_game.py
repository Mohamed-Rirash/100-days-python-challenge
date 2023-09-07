from art import logo
import random

# TODO-1: implement greeting and welcoming the users and print the logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def choose_difficulty():
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if chosen_difficulty == 'easy':
        return 10
    elif chosen_difficulty == 'hard':
        return 5
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        return choose_difficulty()

def compare_guess(user_guess, thinking_number):
    if user_guess > thinking_number:
        return "Too high."
    elif user_guess < thinking_number:
        return "Too low."
    elif user_guess == thinking_number:
        return f"Congratulations! You guessed the correct number: {thinking_number}"
    else:
        return "Please enter only integer numbers"

while True:
    attempts = choose_difficulty()
    thinking_number = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = input("Make a guess: ")
        if not user_guess.isdigit():
            print("Please enter only integer numbers.")
            continue
        user_guess = int(user_guess)
        result = compare_guess(user_guess, thinking_number)
        print(result)

        if result.startswith("Congratulations!"):
            break

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {thinking_number}.")

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
