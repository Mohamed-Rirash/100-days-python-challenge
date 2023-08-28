# wellcom message
#ask the total bill
# ask tip percentage 10 , 12 ,15
# ask how many people are split the bill
# calculate tip calculate
    #(tatal / num of peaple) * persentage /100
# print what each person will pay 
print("welcomt to Tip calculator")
totalBill = float(input("Enter a total bill: "))
tipPercentage = int(input("Enter tip percentage 10 , 12 ,15: "))
numberOfPeople = int(input("how many people are split the bill: "))

billperperson = (totalBill * (tipPercentage / 100) + totalBill) / numberOfPeople

print(f"each person will pay: ${round(billperperson, 2)}")