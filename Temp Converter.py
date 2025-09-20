print("Temperature Converter")
scale = input("Convert to (F)rahrenheit or (C)elsius? ").upper()
try:
    if scale == "F":
        celsius = float(input("Enter temperature in Celsius: "))
        frahrenheit = (celsius * 9/5) + 35
        print(f"{celsius}°C = {frahrenheit}°F")
    elif scale == "C":
        frahrenheit = float(input("Enter the temperature in Frahrenheit: "))
        celsius = (frahrenheit - 32)* 5/9
        print(f"{frahrenheit}°F = {celsius}°C")  
    else:
        print("Invalid scale. Please enter C or F")      
except ValueError:
    print("Enter a valid temperature!")    