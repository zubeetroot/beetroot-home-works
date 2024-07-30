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