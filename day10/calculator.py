print("""
                88                        88                     
                      88                        88              ,d     
                      88                        88              88     
 ,adPPYba, ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM  
a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88     
8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88     
"8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,    
 `"Ybbd8"' `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888                                                                            
                        
 ,adPPYba,  8b,dPPYba,  
a8"     "8a 88P'   "Y8  
8b       d8 88          
"8a,   ,a8" 88          
 `"YbbdP"'  88          
""")
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

# Operators dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
}

# First operation
num1 = int(input("Enter the first number: "))

for operator in operations:
    print(operator)

operation_symbol = input("Choose an operator from the above list: ")
num2 = int(input("Enter the second number: "))

calculation_function = operations[operation_symbol]
f_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {f_answer}")

# Second operation with while loop
while True:
    operation_symbol = input("Choose an operator from the above list (or 'stop' to exit): ").lower()

    if operation_symbol == "stop":
        break

    num3 = int(input("Enter the next number: "))
    calculation_function = operations[operation_symbol]
    f_answer = calculation_function(f_answer, num3)

    print(f"{f_answer} {operation_symbol} {num3} = {f_answer}")