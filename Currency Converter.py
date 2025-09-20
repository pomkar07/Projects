exchange_rate = {
    "USD": 1.0,
    "EUR": 0.85,
    "GPB": 0.75,
    "INR": 74.0,
    "JPY": 110.0,
}
print("Available currancies: USD, EUR, GPB, INR, JPY")
from_currency = input("Convert from: ").upper()
to_currency = input("Convert to: ").upper()

try:
    amount = float(input("Amount to convert: "))
    if from_currency in exchange_rate and to_currency in exchange_rate:
        usd_amount = amount / exchange_rate[from_currency]
        result = usd_amount * exchange_rate[to_currency]
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("Invalid currency cods!")    
except ValueError:
    print("Please enter a valid amount")    