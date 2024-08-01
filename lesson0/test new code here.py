
#Task1: A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".

def favorite_movie():
 print(f"My favorite movie is named The Thing")

favorite_movie()


#Task 2: Creating a dictionary.
#Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.

names = ['Paris', 'Athens', 'Madrid']
capitals = ['France', 'Greece', 'Spain']

def create_and_print_dict():
 country_dict = dict(zip(names, capitals))
 for name, capital in country_dict.items():
  print(f"Country: {name}, Capital: {capital}")

create_and_print_dict()

#Task 2: A simple calculator.

def make_operation()
