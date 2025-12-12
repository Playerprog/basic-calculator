print("Welcome to the Calculator!")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

valid = ["+", "-", "*", "/"]

#only allow valid characters

while True:
    carac = input("Type + or - or * or /): ")
    if carac in valid:
        break
    else:
        print("Choose a valid option!")

#functions for basic calculation types

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2  

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Error: It is not possible to divide by zero!"
    else:
      return n1 / n2

#result of the mathematical operation: 

if carac == "+":
    print(f"The result is: {somar(n1, n2)}")

elif carac == "-":
    print(f"The result is: {subtrair(n1, n2)}")

elif carac == "*":
    print(f"The result is: {multiplicar(n1, n2)}")

elif carac == "/":
    print(f"The result is: {dividir(n1, n2)}")


