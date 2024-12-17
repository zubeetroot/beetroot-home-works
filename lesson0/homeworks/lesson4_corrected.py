#LESSON 4
#TASK 1: String manipulation
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
#Sample String: 'helloworld'
#Expected Result : 'held'
s = "Hello world"
print(len(s))
print(s[:2] + s[-2:])

#Expected Result : 'mymy'
s = "my"
print(s *2)

#Expected Result: Empty String
s = ""
print(s)

#Task 2: Following chunk should be inside of outer if condition:
# if new_string.isdigit(): print("Valid digits") This should also be fixed, please.

new_string = "1234567890"
if len(new_string) == 10:
    print("For string 1: Valid length")
    if new_string.isdigit():
        print("For string 1: Valid digits")
    else:
        print("For string 1: Invalid string!")


new_string = "123456789000000000000000000"
if len(new_string) == 10:
    print("For string 2: Valid length")
    if new_string.isdigit():
            print("For string 2: Valid digits")
    else:
            print("For string 2: Invalid string!")

new_string = "aaaaaa1"
if len(new_string) == 10:
    print("For string 3: Valid length")
    if new_string.isdigit():
        print("For string 3: Valid digits")
    else:
        print("For string 3: Invalid string!")

#Task 3: The name check.
#Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
#The program should check if your input is equal to the stored name even if the given name has another case,
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
stored_name = "zuza"
new_name = input("Enter your name here:")
print(f"You've entered: ", new_name)
if new_name.lower() == stored_name:
    print("New and stored are the same: ", new_name.lower())
    print(True)
else:
    print("New name different from stored name: ", new_name.upper())
    print(False)



