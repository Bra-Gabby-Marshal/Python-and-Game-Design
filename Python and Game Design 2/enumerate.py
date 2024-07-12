# Enumerate in Python
# enumerate() is a built-in Python function used to loop over an iterable object while keeping track of the index of each item. 
# It returns an enumerate object, which is an iterator of tuples containing the index and the value from the iterable.

my_list = ['a', 'b', 'c', 'd']

for index, value in enumerate(my_list):
        print(f"Index: {index}, Value: {value}")

# Ex 2
myFruits = ["banana", "apple", "orange", "mango"]

for index, fruit in enumerate(myFruits, start=1):
        print(f"friut {index} : {fruit}")