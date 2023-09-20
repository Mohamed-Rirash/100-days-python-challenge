psize = input("Enter your pizza size: (S, M, L): ").upper()
add_perperonic = input("Do you want to add pepperoni: (Y/N): ").upper()
extra_cheese = input("Do you want to add extra cheese: (Y/N): ").upper()

small_pizza = 15
medium_pizza = 20
large_pizza = 25

perperonic_small = 2
perperonic_medium_and_large = 3

extra_cheese_cost = 1

if psize == "S":
    if add_perperonic == "Y":
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${small_pizza + perperonic_small + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${small_pizza + perperonic_small}")
    else:
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${small_pizza + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${small_pizza}")

elif psize == "M":
    if add_perperonic == "Y":
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${medium_pizza + perperonic_medium_and_large + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${medium_pizza + perperonic_medium_and_large}")
    else:
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${medium_pizza + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${medium_pizza}")

elif psize == "L":
    if add_perperonic == "Y":
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${large_pizza + perperonic_medium_and_large + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${large_pizza + perperonic_medium_and_large}")
    else:
        if extra_cheese == "Y":
            print(f"The price of your pizza is ${large_pizza + extra_cheese_cost}")
        else:
            print(f"The price of your pizza is ${large_pizza}")
