import math
from os import system

while True:
    operation = input("Enter your operation (+, -, *, /, source, high): ")
    first = float(input("Enter your first number: "))

    if operation == "+":
        second = float(input("Enter your second number: "))
        total = first + second
    elif operation == "-":
        second = float(input("Enter your second number: "))
        total = first - second
    elif operation == "*":
        second = float(input("Enter your second number: "))
        total = first * second
    elif operation == "/":
        second = float(input("Enter your second number: "))
        if second != 0:
            total = first / second
        else:
            total = "Division by zero is not allowed"
    elif operation == "source":
        total = math.sqrt(first)
    elif operation == "high":
        second = float(input("enter the number to be raised: "))
        total = math.pow(first, second)
    else:
        total = "Please enter a valid operation"

    print("Your operation result is:", total)

    choice = input("Do you want to perform another operation? (y/n): ")
    if choice.lower() != "y":
        break