import random

number_to_guess = random.randint(1, 10)
attempts = 0
guess = None

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number_to_guess}.")
            print(f"You guessed it in {attempts} attempts.")
        print("Please enter a valid number!")