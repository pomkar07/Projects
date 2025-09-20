#get the user current year and birth year
birth_year = int(input("Please enter your birth year: "))
current_year = int(input("Please enter your current year: "))

#validate and calculate
if birth_year and current_year:
    age = current_year - birth_year
    print(f"Your age is {age}")
else:
    print("Please enter a valid number")