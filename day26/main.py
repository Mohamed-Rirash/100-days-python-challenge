student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# data = pandas.read_csv("day26/nato_phonetic_alphabet.csv")


# # datadic = {letter:code.to_dict() for letter,code in data.iterrows()}
# data_dict = dict(zip(data['letter'], data['code']))


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# user_name = input("what is your name: ").upper()

# user_name_lsit = [letter for letter in user_name.split(" ")]

# result = [data_dict.get(letter, letter) for letter in user_name if letter.isalpha()]

# print(result)


import pandas

data = pandas.read_csv("day26/nato_phonetic_alphabet.csv")



while True:


# #TODO 1. Create a dictionary in this format:
    phenatic_dict = {row.letter:row.code for (index, row) in data.iterrows()}



# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    try:
        user_name = input("what is your name: ").upper()
        resutl = [phenatic_dict[letter] for letter in user_name ]
    except KeyError:
        print("pleae insert only charecters")
    else:
        print(resutl)
        break
