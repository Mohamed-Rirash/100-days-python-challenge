weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight / height ** 2
print(f"your body mass index is {bmi}")


if bmi < 18.5:
    print("Your are underweight!\n Please eat more")
elif bmi > 18.5:
    if bmi < 25:
        print("your weight is normal")
elif bmi > 25:
    if bmi < 30:
        print("you are overweight")
elif bmi > 30:
    if bmi < 35:
        print("you are obese")
elif bmi > 35:
    print("you are clinically obese")
else:
    print("please check your weight and height ")
