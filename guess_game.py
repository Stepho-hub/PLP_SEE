import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Let the user guess
guess = int(input("Take a guess: "))

# Check the guess
if guess == secret_number:
    print("🎉 Correct! You guessed the number!")
else:
    print(f"❌ Sorry, the correct number was {secret_number}. Better luck next time!")
    