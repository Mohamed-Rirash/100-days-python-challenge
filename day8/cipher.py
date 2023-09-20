alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
   

#++++++++++++++++++++++++++++++original code+++++++++++++++++++++++++++++++++++++++++++++++++++

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#         else:
#             cipher_text += letter
#     print(f"Encoded text: {cipher_text}")
#     return cipher_text

# def decrypt(encrypted_text, shift_amount):
#     decoded_text = ""
#     for letter in encrypted_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#             decoded_text += new_letter
#         else:
#             decoded_text += letter
#     print(f"Decoded text: {decoded_text}")
#     return decoded_text

# if direction == "encode":
#     encrypted_text = encrypt(text, shift)
# elif direction == "decode":
#     decrypted_text = decrypt(text, shift)
# else:
#     print("Please choose one of the options: 'encode' or 'decode'")


   
