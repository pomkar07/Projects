weight = int(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")

if bmi <= 18:
    print("You are underwight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("Enter valid number")            