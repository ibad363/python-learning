import random

print("🎯 Welcome to the Number Guessing Game! 🎯")
print("You have 5 attempts to guess a number between 50 and 100. Let's begin!")

max_attempts = 5
attempts = 0
secret_number = random.randint(50, 100)

while attempts < max_attempts:
    attempts += 1
    user_guess = int(input("Enter your guess: "))

    if user_guess == secret_number:
        print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempt(s).")
        break
    elif attempts >= max_attempts:
        print(f"😞 Game Over! The correct number was {secret_number}. Better luck next time!")
    elif user_guess < secret_number:
        print("🔽 Too low! Try again.")
    else:
        print("🔼 Too high! Try again.")