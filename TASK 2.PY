
import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))


secret_number = random.randint(low, high)

print(f"\nI'm thinking of a number between {low} and {high}.")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number!")
        break
