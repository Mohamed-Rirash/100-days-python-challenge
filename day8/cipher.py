alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# ==============Compressed===============================================
def cipher(text_message, shift_amount, direction):
    end_text = ""
    if direction == "decode":
         shift_amount *= -1
    for letter in text_message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"{direction} text: {end_text}")


cipher(text, shift, direction)





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


   
