import random

print("Guess a number 1 and 10")
secret_number = random.randint(1, 10)

try: 
    guess = int(input("your guess: "))

    if guess == secret_number:
        print("Congratulations! you guess it right")
    else:
        print("You are wrong")
except ValueError:
    print("Enter valid output")             