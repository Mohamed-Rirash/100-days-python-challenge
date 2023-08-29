print("Welcome to the Enigmatic Island - Gate One")

gate1 = int(input("Choose one of the two gates: (1/2)"))

if gate1 == 1:
    print("Well done!")
    gate2 = int(input("Choose one of the three gates: (1/2/3)"))

    if gate2 == 1:
        print("You found a room full of treasures, including a valuable laptop.")
        print('''
    ______________
   ||            ||
   ||            ||
   ||            ||
   ||            ||
   ||____________||
   |______________|
    \\############\\
     \\############\\
       \      ____    \   
        \_____\___\____\ ''')

        key_choice = int(input("You've also uncovered a locked chest. To unlock it, choose a key: (1)Gold key or (2)Silver key: "))

        if key_choice == 1:
            print("Congratulations, you found the hidden treasure! YOU WIN!")

        else:
            print("The chest remains locked. You must find the correct key to access the treasure.")
        
    elif gate2 == 2:
        print("Oh no! A trapdoor opens beneath you. You fall into a pit.\nGAME OVER!")

    else:
        print("You entered a room with a sleeping dragon.")
        approach = int(input("Do you want to (1)sneak around the dragon or (2)try to steal its treasure?"))

        if approach == 1:
            print("You successfully sneak around the dragon and find a room with the treasure!\nCongratulations, you found the hidden treasure! YOU WIN!")
        else:
            print("The dragon wakes up and devours you.\nGAME OVER!")

elif gate1 == 2:
    print("The time machine has transported you to the Forbidden Desert Island.")
    gate3 = int(input("Choose one of the two gates: (1/2)"))

    if gate3 == 1:
        wait = int(input("There is a sudden flood. Do you want to (1)wait or (2)attempt to cross?"))

        if wait == 1:
            print("The flood subsides, and you discover a hidden boat!")
            print("You row across the water and reach a secluded island.")
            gate5 = int(input("Choose one of the two doors: (1)left door or (2)right door"))

            if gate5 == 1:
                print("You entered a room full of wild animals.\nGAME OVER!")
            else:
                print("Congratulations, you found the hidden treasure on the secluded island!")

                final_challenge = int(input("To claim the treasure, solve this riddle:\nI speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (1)Echo (2)Shadow (3)Fire"))

                if final_challenge == 1:
                    print("You've successfully solved the riddle and claimed the treasure! YOU WIN!")
                else:
                    print("The riddle remains unsolved, and the treasure stays hidden.\nGAME OVER!")

        else:
            print("You were swept away by the flood.\nGAME OVER!")

    else:
        gate4 = int(input("Three men stand before you:\n(1)A brawny man with no weapons.\n(2)A man with a vial of instant poison.\n(3)A man with a gleaming knife.\nWhich one do you confront? "))

        if gate4 == 1 or gate4 == 3:
            print("They overpower you, and you're unable to escape!\nGAME OVER!")
        else:
            print("You skillfully evade the poison and defeat the knife-wielding man.")
            print("You discover a set of keys.")
            gate6 = int(input("Choose one key:\n(1)Red\n(2)Blue\n(3)Green"))

            if gate6 == 1:
                print("You unlock a room filled with roaring flames!\nGAME OVER!")

            elif gate6 == 2:
                print("You unlock a door that leads to the vast ocean.")
                gate7 = int(input("Do you want to (1)swim to the coast or (2)search for a boat?"))

                if gate7 == 1:
                    print("You are attacked by ferocious sharks.\nGAME OVER!")
                else:
                    print("Regrettably, there are no boats on the coast.\nGAME OVER!")

            else:
                print("You unlock a room filled with impenetrable jungle!\nGAME OVER!")

else:
    print("You meet an unfortunate fate due to your wrong choice!\nGAME OVER!")
