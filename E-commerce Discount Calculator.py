#Calcute final price after discount
original_price = 10.99
discount_percentage = 15 # in percentage
discount_amt = original_price * (discount_percentage / 100)
final_price = original_price - discount_amt
print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}") 