#TASK 1:The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random

random_number = random.randint(1, 3)

your_guess = input("Enter your guess: ")
print(type(int((input)))

if your_guess != random_number:
    print(f"You guessed it wrong! I was thinking of: ", random_number)
else:
    print("You got it right!")
