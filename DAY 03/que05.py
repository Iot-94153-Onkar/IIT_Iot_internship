
def greet(name, msg="Hello"):
    print(msg, name)



def info(name, age):
    print("Name:", name)
    print("Age:", age)



def add(a, b):
    return a + b


def operate(func, x, y):
    return func(x, y)



greet("ONKAR")
greet("ONKAR", msg="HI")

info(age=22, name="ONKAR")

print("Result:", operate(add, 5, 3))
