print("Welcome to Treasure Island - Gate One")
gate1 = int(input("Choose one of the two gates: (1/2)"))

if gate1 == 1:
    print("Well done!")
    gate2 = int(input("Choose one of the three gates: (1/2/3)"))
    if gate2 == 1:
        print("You found a room full of treasures! with laptop")
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
        print("Congratulations, you found the hidden treasure! YOU WIN!")
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
    print("The time machine has taken you to the Desert Island.")
    gate3 = int(input("Choose one of the two gates: (1/2)"))
    if gate3 == 1:
        wait = int(input("There is a flood. Do you want to (1)wait or (2)try to cross?"))
        if wait == 1:
            print("The flood subsides, and you find a boat!")
            print("You row across the water and reach a hidden island.")
            gate5 = int(input("Choose one of the two doors: (1)left door or (2)right door"))
            if gate5 == 1:
                print("You entered a room full of wild animals.\nGAME OVER!")
            else:
                print("Congratulations, you found the hidden treasure on the hidden island! YOU WIN!")
        else:
            print("You were swept away by the flood.\nGAME OVER!")
    else:
        gate4 = int(input("There are three men in front of you!\n(1)A muscular man with no weapons.\n(2)A man with a poison that kills instantly.\n(3)A man with a knife.\nWhich one do you face? "))
        if gate4 == 1 or gate4 == 3:
            print("They overpower you, and you're unable to escape!\nGAME OVER!")
        else:
            print("You successfully dodge the poison and defeat the man with the knife.")
            print("You find a set of keys.")
            gate6 = int(input("Choose one key: \n(1)Red\n(2)Blue\n(3)Green"))
            if gate6 == 1:
                print("You unlocked a room filled with fire!\nGAME OVER!")
            elif gate6 == 2:
                print("You unlocked a door that leads to the ocean.")
                gate7 = int(input("Do you want to (1)swim to the coast or (2)look for a boat?"))
                if gate7 == 1:
                    print("You were attacked by sharks.\nGAME OVER!")
                else:
                    print("Unfortunately, there are no boats on the coast.\nGAME OVER!")
            else:
                print("You unlocked a room filled with dense jungle!\nGAME OVER!")

else:
    print("You died for making the wrong choice!\nGAME OVER!")
