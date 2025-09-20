#please enter your password
password = input("Enter your password: ")

has_letter = any(char.isalpha() for char in password)
has_digit = any(char.isdigit() for char in password)

if has_letter and has_digit:
    print("Strong password")
elif has_letter:
    print("Please include number")
elif has_digit:
    print("Please include character")
else:
    print("Please include both")            