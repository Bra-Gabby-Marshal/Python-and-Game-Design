# Mutation in python
# In Python, mutation refers to changing the state of an object.
# Mutable objects can be modified after they are created, while immutable objects cannot be changed after they are created.

# Mutating a list
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

# Mutating a dictionary
my_dict = {'a': 1, 'b': 2}
my_dict['a'] = 100
print(my_dict)

# Mutating a set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
