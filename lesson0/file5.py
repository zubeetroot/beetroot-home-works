
x = 111
print(x)
def test(x):
    x += 4
    print("This is x inside funct: ", x)
    return x

x = test(x)
print(x)

import random

def random_math(a: 66, b: 67):
    def add():
        return a+b
    def sub():
        return a-b

    def mul():
        return a*b

    def div():
        return a/b

    return random.choice([add, sub, mul, div])

func = random_math(3, 2)
print(func())
