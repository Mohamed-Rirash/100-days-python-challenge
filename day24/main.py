#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# names_list = []
# with open("day24/Input/Letters/starting_letter.txt") as letters:
#     with open("day24/Input/Names/invited_names.txt") as names:
#        for name in names.readlines():
#            names_list.append(name.strip())
    
#     content = letters.readline()
#     for i in names_list:
#         letter_name = content.replace("[name]", i)
#         print(letters.read())
        
names_list = []

with open("day24/Input/Letters/starting_letter.txt") as letters:
    with open("day24/Input/Names/invited_names.txt") as names:
        for name in names.readlines():
            names_list.append(name.strip())

    content = letters.read()  

for name in names_list:
    letter_name = content.replace("[name]", name)
    
    
    letter_with_name = f"{letter_name}\n"

    with open(f"day24/Output/ReadyToSend/letter_for_{name}.txt","w") as aut_letter:
        aut_letter.write(letter_with_name)



### i will refector this latter