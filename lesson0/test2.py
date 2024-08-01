from unittest import result



num1 = 5
num2 = 5


def make_operation(operation, num1, num2, num3):
    if operation == "+":
        return num1 + num2 + num3
    elif operation == "*":
        return num1 * num2 * num3

result = make_operation("*", num1, num2, num3)
print(result)