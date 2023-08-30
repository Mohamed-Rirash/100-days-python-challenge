import random

number_of_letters = int(input("How many letters you need: "))
number_of_symbols = int(input("How many symbols would you like: "))
number_of_numbers = int(input("How many numbers you need: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")","+","-"]

# sellect k number of random char from the lists
random_letters = random.sample(letters, number_of_letters)
random_numbers = random.sample(numbers, number_of_numbers)
random_symbols = random.sample(special_symbols_list, number_of_symbols)

# Concatenate the lists of characters to form the password
password_list = random_letters + random_numbers + random_symbols

# Shuffle the password list
random.shuffle(password_list)

# Convert the shuffled list back to a string
password = ''.join(password_list)

print("Generated password:", password )
