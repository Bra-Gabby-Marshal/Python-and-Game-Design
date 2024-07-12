# Tuple
# mytuple = ("apple", "banana", "melons")

# # Tuple Unpacking: allows to assign the values of a tuple to multiple variables in a single line of code
# tupleUnpack = (3, 5)
# x, y = tupleUnpack

# print('output of x : ', x)
# print('output of y : ', y)

# # Exampl 2
# coordinates = (0.05, 5.4, 7.8)
# # a, b, c = coordinates
# b, c, a = coordinates
# print('coordinates of b : ', b)
# print('coordinates of c : ', c)
# print('coordinates of a : ', a)

# # Interactions between Python Functions:It interact with each other in various ways. They can call one another, pass values as arguments, return values
# def greet(name):
#     return f"Hello, {name}!"

# def welocome():
#     return "Welcome to Python & Game Design 2"

# def start():
#     name = input("Enter your name:")
#     print(greet(name))
#     print(welocome())

# start()


# *args and **kwargs: These are special syntaxes in Python that allow a function to accept a variable number of positional arguments (*args) and keyword arguments (**kwargs)
# *args (or “variable-length positional arguments”): This syntax allows a function to receive any number of positional arguments. The arguments are passed to the function as a tuple.
# **kwargs (or “variable-length keyword arguments”): This syntax allows a function to receive any number of keyword arguments. The arguments are passed to the function as a dictionary.

def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\n Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, 3, name="Lios", age=25)