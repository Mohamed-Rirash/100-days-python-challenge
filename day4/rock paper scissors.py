import random
userchoose = int(input("what did you choose (0) for rock (1) for paper (2) for scissors: "))
computer_choose = random.randint(0,2)

rock = ''''
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

scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

    # computer


if userchoose == 0 and computer_choose == 0:
    print(f"user choose: {userchoose}\n {rock}")
    print(f"Computer choose: {computer_choose}\n {rock}")
    print("this is Draw")
elif userchoose == 0 and computer_choose == 2:
    print(f"user choose: {userchoose}\n {rock}")
    print(f"Computer choose: {computer_choose}\n {scissor}")
    print(" user win")
elif userchoose == 0 and computer_choose == 1:
    print(f"user choose: {userchoose}\n {rock}")
    print(f"Computer choose: {computer_choose}\n {paper}")
    print("tComputer win")



elif userchoose == 1 and computer_choose == 0:
    print(f"user choose: {userchoose}\n {paper}")
    print(f"Computer choose: {computer_choose}\n {rock}")
    print(" computer win")
elif userchoose == 1 and computer_choose == 2:
    print(f"user choose: {userchoose}\n {paper}")
    print(f"Computer choose: {computer_choose}\n {scissor}")
    print(" user win")
elif userchoose == 1 and computer_choose == 1:
    print(f"user choose: {userchoose}\n {paper}")
    print(f"Computer choose: {computer_choose}\n {paper}")
    print("this is drow")


elif userchoose == 2 and computer_choose == 0:
    print(f"user choose: {userchoose}\n {scissor}")
    print(f"Computer choose: {computer_choose}\n {rock}")
    print(" computr win")
elif userchoose == 2 and computer_choose == 2:
    print(f"user choose: {userchoose}\n {scissor}")
    print(f"Computer choose: {computer_choose}\n {scissor}")
    print("this is draw")
elif userchoose == 2 and computer_choose == 1:
    print(f"user choose: {userchoose}\n {scissor}")
    print(f"Computer choose: {computer_choose}\n {paper}")
    print("user win")
else:
    print("wrong choose!: ")





