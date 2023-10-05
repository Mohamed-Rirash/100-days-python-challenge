numbers = [1,1,2,3,5,8,13,21,34,55]

#TODO 1: LIST OF ENVEN NUMBERS


squered_numbers = [n**2 for n in numbers]

print(squered_numbers)



#TODO 2: LIST OF ENVEN NUMBERS
result = [n for n in numbers if n %2 == 0]
print(result)


#TODO 3 mached numbers from the two files

# read the two files 
with open("day26/file1.txt") as file1:
    file1_list = [num.strip() for num in file1]

with open("day26/file2.txt") as file2:
    file2_list = [num.strip() for num in file2]

    
# compare them and fine the mached once
result  = [num for num in file1_list if num in file2_list]


print(result)
#$$$$$$$$$$$$$$$$$$$$$$$$$$ ___Disctionary COMPREHENSION$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
student_scores = {
    "John": 85,
    "Alice": 92,
    "Bob": 44,
    "Eve": 95,
    "Charlie": 34
}

passed_students = {student: score for student, score in student_scores.items() if score > 50}

#TODO:1:

sentence = "Feel free to let me know if you'd like another sentence or if you have any specific requests."


result = {word:len(word) for (word) in sentence.split(" ") }

print(result)


#TODO:1: temperature convertor

week_temperatures = {
    "Monday": 75,
    "Tuesday": 78,
    "Wednesday": 82,
    "Thursday": 79,
    "Friday": 85,
    "Saturday": 88,
    "Sunday": 87
}

weather_f = {days:(temp_in_c * 9/5) + 32 for days,temp_in_c in week_temperatures.items()}

print(weather_f)





