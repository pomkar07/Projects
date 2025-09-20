#Problem 1: Temperature Conversion
Fahrenheit_temp = 78 # in °F
celsius = (Fahrenheit_temp - 32) * 5/9
print(f"Celsius {celsius:.0f}°C = Fahrenheit {Fahrenheit_temp}°F") 

#Problem 2: Shopping Cart Calculator
book = 15.50 
notebook = 5.75
pen = 1.25
tax = 8.5 
tax_rate = (book + notebook + pen) * tax / 100
total_amt = (book + notebook + pen + tax_rate)
print(f"Your tax amount is {tax_rate:.2f}")
print(f"Your total amount is {total_amt:.2f}")

#Problem 3: User Information Form
first_name = "Omkar"
last_name = "Patil"
age = 20
email = "pomkar1811@fake.com"
print(f"First name: {first_name} last Name: {last_name} Age: {age} Email address: {email}")

#Problem 4: Simple Interest Calculator
principle = 2500
rate = 3.5 #in %
time = 5 #in years 
interest = (principle * rate * time) / 100
total_amt = principle + interest
print(f"Interest earned is ${interest:.2f} and total amount is ${total_amt:.2f}")

#Problem 5: Time Converter 
#i had to google this since i do not know how to convert sec into hours and min
total_sec =  7385
hours = total_sec / 3600
min = hours / 60 
sec = min 
print(f"{total_sec:.0f} seconds = {hours:.0f}hours, {min:.0f}minutes, {sec:.0f}seconds")