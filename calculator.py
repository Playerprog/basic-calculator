print("Welcome to the Calculator!")

# simple menu to choose the operation

def menu():
    print("1 - sum")
    print("2 - subtracion")
    print("3 - multiplication")
    print("4 - division")

# functions for basic calculation types

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2  

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2


while True:    
    
    menu()

# operation validation
    
    while True:
        
        valid_operation = ["1", "2", "3", "4"]
        
        print("Choose the number that corresponds to your operation:")
        
        operation = input()
        if operation in valid_operation:
            break
        print("Invalid operation!")

    while True:
        try:
            n1 = float((input("Enter the first number: ")))
            n2 = float((input("Enter the second number: ")))
            
            if operation == "4" and n2 == 0:
                print("Denominator cannot be 0")
                continue
                
            break
        except ValueError:
            print("Enter only numbers, not")

    
#result of the mathematical operation: 

    if operation == "1":
        print(f"The result is: {somar(n1, n2)}")

    elif operation == "2":
        print(f"The result is: {subtrair(n1, n2)}")

    elif operation == "3":
        print(f"The result is: {multiplicar(n1, n2)}")

    elif operation == "4":
        print(f"The result is: {dividir(n1, n2)}")
    
# program end option

    print("Do you want to stop running the program?")
    finish = input().lower()
    if finish == "yes":
        break
    elif finish != "no":
        print("Invalid operation!")


