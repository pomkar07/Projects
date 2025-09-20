#enter the temperature in fahrenherit
temp_fahrenherit = float(input("Please enter the temperature in fahrenherit: "))
#calculate
temp_celsius = (temp_fahrenherit - 32) * 5/9
print(f"{temp_fahrenherit:.2f}°F = {temp_celsius:.2f}°C")