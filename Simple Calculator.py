#enter 2 number for calculation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation(+,-,*,/): ")

#calculate 
if operation == "+":
 print(num1 + num2)
elif operation == "-":
 print(num1 - num2)
elif operation == "*":
 print(num1 * num2)
elif operation == "/":
 print(num1 / num2)
else:
 print("Please enter valid operation")