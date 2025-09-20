#Age Calculator with Validation
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter your current year: "))

age = current_year - birth_year
if age == int:
    print(f"Your age is {age}")
else:
    print("Enter a valid input") 

#Temperature Converter with Input
celsius = int(input("Enter your temperature: "))

fahrenheit = (celsius * 9/5) + 35
print(f"{celsius}°C = {fahrenheit}°F")

#String Number Adder
num1 = input("Enter your number 1: ")
num2 = input("Enter your number 2: ")

num1 = int(num1)
num2 = int(num2)

print("num1 + num2")

#Boolean Converter
student_name = ""
student_name = bool(student_name)
print(student_name)

student_age = 21
student_name = bool(student_name)
print(student_age)

student_cgpa = ""
student_name = bool(student_name)
print(student_cgpa)

student_gender = "male"
student_name = bool(student_name)
print(student_gender)

student_last_name = ""
student_name = bool(student_name)
print(student_last_name)

#Mixed Type Calculator
value1 = input("Enter your first value: ")
value2 = input("Enter your second value: ")

if value1 == str and value2 == str:
    print(value1 + value2)
elif value1 == int and value2 ==int:
    value1 = int(value1)
    value2 = int(value2)
    print(value1 + value2)
else:
    print("Error you noob")        