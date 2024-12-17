#Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops(list1, index):
    try:
        return list1[index]
    except IndexError:
        return "Index out of range"

list1 = [1, 2, 3]

specific_element = oops(list1, 4)
print(f"Element at index 1: {specific_element}")


if specific_element == "Index out of range":
    print("Error caught: Index out of range")

#Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
# the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by
# the input function were not numbers, and if value b was zero (cannot divide by zero).

#???????? FAILED TASK ????????

import math
def squaring_and_dividing(a, b):
	result = (a ** 2) / b
	return result
def enter_input():
	try:
		a = int(input("Enter the first number: "))
		b = int(input("Enter the second number: "))
		return a, b
	except ValueError:
		return print("Error: both inputs must be digits")
	except ZeroDivisionError:
		return print("Error: Division by zero is not allowed.")

a, b = enter_input()
print("Here is the result: ", squaring_and_dividing(a, b))
