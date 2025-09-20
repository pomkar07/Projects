import random

secret_number = random.randint(1,10)
guess_number = int(input("Guess a number between 1 and 10: "))

if guess_number == secret_number:
    print("Congratulations! You guessed it!")
else:
    print(f"Wrong! The number was {secret_number}.")    