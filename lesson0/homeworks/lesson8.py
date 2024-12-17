#Task1: A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".

def favorite_movie():
 print(f"My favorite movie is named The Thing")

favorite_movie()




print()
#Task 2: Creating a dictionary.
#Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.

capitals = ['Berlin', 'Athens', 'Madrid']
names = ['Germany', 'Greece', 'Spain']

def create_and_print_dict():
 country_dict = dict(zip(names, capitals))
 for name, capital in country_dict.items():
  print(f"Country: {name}, Capital: {capital}")

create_and_print_dict()




print()
#Task 3: A simple calculator.
#Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter and an arbitrary number of arguments (only numbers) as the second parameter.
#Then return the sum or product of all the numbers in the arbitrary parameter

num1 = 7
num2 = 9
num3 = 2

def make_operation(operation, num1, num2, num3):
    if operation == "+":
        return num1 + num2 + num3
    elif operation == "*":
        return num1 * num2 * num3
    else:
        return "Invalid operation"

result = make_operation("+", num1, num2, num3)
print("Result of the operation:", result)



#ANSWERS:
#My favorite movie is named The Thing

#Country: Germany, Capital: Berlin
#Country: Greece, Capital: Athens
#Country: Spain, Capital: Madrid

#Result of the operation: 18