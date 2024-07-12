# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression.

# # Example to Add 10 to the argument a, and return the result:

# damien = lambda a : a + 10
# print(damien(2))

# x = lambda c : c + 4
# print(x(2))

# # Ex 
# #  Add 20 to argument b,  and return the result:
# v = lambda b : b + 20
# print(v(3))
# #  Add 30 to argument b,  and return the result:
# d = lambda b : b + 30
# print(d(20))

# Map Function
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# numbers = [ 1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)


# Double all numbers using map and lambda
# numbers = (1, 2, 3, 4, 5)
# double_numbers = map(lambda x: x + x, numbers)
# print(list(double_numbers))

# Add two lists using map and lambda
# number1 = [1, 2, 3, 4]
# number2 = [5, 6, 7, 1]
# number3 = [8, 9, 10, 11]
# results = map(lambda x, y, z: x + y + z, number1, number2, number3)
# print(list(results))


# Nested Statements and Scope
# x = 10 # Global variable

# def outer_function():
#     y = 20

#     def inner_function():
#         z = 30
#         print("Inner Function: ", x,y,z)

#     inner_function()
#     print("Outer Function: ", x,y)

# outer_function()
# print("Global Scope: ", x)

# def outer_function():
#     x = 30

#     def inner_function():
#         y = 40
#         print("Inner Function: ", x,y)

#     inner_function()
#     print("Outer Function" , x)

# outer_function()

# Global and Local Scope
# x = 10

# def myFunction():
#     global x # Declare x as global within the function
#     x = 20 # Modify the global variable x
#     y = 30 # Local Variable

#     def inner_function():
#         z = 40 
#         print("Inner Function: ", x, y, z)

#     inner_function()
#     print("Outer Function", x, y)

# myFunction()
# print("Global Scope", x)
        

# Python Objects and Data Structure Basics
# They are containers that organize and group data according to type

# Lists
myList = [1, 2, 3, 4, 5]
print(myList)

# Tuple
myTuples = (1, 2, 3)
print(myTuples)
