students_height = input("enter a list of students height: ").split()

for n in range(0, len(students_height)):
    students_height[n] =int(students_height[n])
print(students_height)

total = 0
count = 0

for student_height in  students_height:
     total += student_height
     count += 1
     avg = total/ count

print(f"the average height of students is : {round(avg)}")