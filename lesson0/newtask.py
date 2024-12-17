


#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.


def word_count(str):
    counts = dict()

    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

import functools
print( word_count('To już ten moment. Czas na otwarcie igrzysk olimpijskich'))


num1 = 7
num2 = 7
num3 = 2

def make_operation(operation, num1, num2, num3):
    if operation == "+":
        return num1 + num2 + num3
    elif operation == "*":
        return num1 * num2 * num3
    else:
        return "Invalid operation"

result = make_operation("+", num1, num2, num3)
print(result)