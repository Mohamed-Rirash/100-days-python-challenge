import random
namesString= input("enter all names seperated by (, and space): ")

names = namesString.split(", ")

print(names)

randouemval = random.randint(0, len(names))

payBill = names[randouemval]

print(payBill)

