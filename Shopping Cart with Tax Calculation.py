item_price = int(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))
tax_rate = int(input("Enter tax rate: "))

subtotal = item_price * quantity
tax_amt = subtotal * (tax_rate/100)
total = subtotal + tax_amt

print(f"Subtotal: {subtotal}")
print(f"Tax Amount: {tax_amt}")
print(f"Total: {total}")
