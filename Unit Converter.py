value = int(input("Please enter to convert: "))
unit = input("Enter current unit (km/miles): ").lower()

if unit == "km":
    miles = value * 0.621371
    print(f"{miles:.2f}miles == {value}km")
elif unit == "miles":
    km = value * 1.60934
    print(f"{km:.2f}km == {value}miles")
else:
    print("Enter valid unit")