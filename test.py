#Problem 1: Personal Information Collector
print("Hi Welcome to our Page")
print("Please enter your personal information:")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
profession = input("Enter your profession: ")

print("Summary of your information")
print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Your city name is {city}")
print(f"Your profession is {profession}")

#Problem 2: Simple Calculator with Validation
print("Calculator")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second: "))
operation = input("Enter your operation: ")

try:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2 
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print(f"Error not divison by 0")
        else:
            result = num1 / num2
    else:
        print("Invaid number or operation")
except ValueError:
    print("Invalid Operator")    

#Problem 3: Temperature Converter with Choice
print("Temperature Checker")
scale = input("Convert to (F)rahrenheit or (C)elsius? ")

try:
    if scale == "C":
        frahrenheit = float(input("Enter the temperature in Frahrenheit: "))
        celsius = (frahrenheit - 32)* 5/9
        print(f"{frahrenheit}°F = {celsius}°C")
    elif scale == "F":
        celsius = float("Enter temperature in Celsius: ")
        frahrenheit = (celsius * 9/5) + 35
        print(f"{celsius}°C = {frahrenheit}°F")
    else:
        print("Invalid errror")        

except ValueError:
    print("Invalid error")   

#Problem 4: Mad Libs Story Game
print("Welcome to Madlibs")

name = input("Enter your name: ")
place = input("Enter your place: ")

print(f"Our boy name was {name}he went to {place}")

#Problem 5: Number Guessing Game with Hints
import random
secret_number = random.randint(1,100)

guess = int(input("Please enter your number: "))

try:

    if guess == secret_number:
        print("Right")
    else:
        print("Wrong")    

except ValueError:
    print("Error wrong inout")    