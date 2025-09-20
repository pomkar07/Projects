print("Simple login system")
username = input("Create a username: ")
password = input("Create a password: ")

print("\nAccount created successfully")
print("Please login")
input_username = input("Username: ")
input_password = input("Password: ")

if input_username == username and input_password == password:
    print("Login successful! Welcome!")
else:
    print("Invalid username or password")    