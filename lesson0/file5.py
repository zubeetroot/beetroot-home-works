x = 111
def test(x):
    x += 1
    print("here is x inside a function: ", x)
#you should understand: scope of function is only changed within the function
test(x)
print(x)


# global = global scope = it exists and increases the scope of data taken into account by the code, BUT it's fron
def test2():
    y = 101
    print("here is x inside a function: ", x)
print(y)

defining x





#TASK 2: The birthday greeting program.
#Write a program that takes your name as input, and then your age as input and greets you with the following:
# "Hello <name>, on your next birthday you’ll be <age+1> years"

name = "Zuza"
age = 25
number_to_add = 1
message = f"Hello {name}, on your next birthday you'll be {(age)+(number_to_add)} years old"
print(message)

print("end of task 2")

#TASK 3: Words combination
#Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string. For example, the program obtained the word ‘hello’, so it should print
# 5 random strings(words) that combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)


import random
import string

input_string = "hello"
string_length = len(input_string)

for i in range(string_length):
    random_letter = random.choice(list(input_string))
    print(random_letter)

print("end of task 3")
#TASK 4: The math quiz program
#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

a = 10
b = 10


print(a + b)
user_answer = "30"

if user_answer == (a + b):
    print("That is correct")
else:
    print(f"Your answer {user_answer} is wrong, the correct answer is {a + b}")

