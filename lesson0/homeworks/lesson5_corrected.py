#TASK 1:The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random

random_number = random.randint(1, 3)

your_guess = input("Enter your guess: ")

if int(your_guess) != random_number:
    print(f"You guessed it wrong! I was thinking of: ", random_number)
else:
    print("You got it right!")

#TASK 3: Words combination
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
#Tips: Use random module to get random char from string)

import random
import string

input_string = "Greetings"
string_length = len(input_string)

for i in range(string_length):
    random_letter = random.choice(list(input_string))
    random.shuffle(random_letter)
    print("Randomised string 1:", random_letter)

print("")
for i in range(string_length):
    random_letter = random.choice(list(input_string))
    random.shuffle(random_letter)
    print("Randomised string 2:", random_letter)


