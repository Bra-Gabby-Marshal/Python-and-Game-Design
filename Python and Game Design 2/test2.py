# Dictionary Comprehension

# Example
# myDict = {'name': 'Lios', 'age':'13', 'class': 'JHS 2'}
# print("Keys:", myDict.keys())
# print("Values:", myDict.values())
# print("Items:", myDict.items())

# Using the items()method
# myDictionary = {'a':1, 'b': 2, 'c': 3, 'd': 4}
# myNewDict = {value:key for (key,value) in myDictionary.items()}
# print(myNewDict)

# Example
# names =['Lios', 'Aarnik', 'Daniel', 'Damien', 'Lilian']
# nameLengths = {name: len(name) for name in names}
# print(nameLengths)

# Assignment
# Write a code to count charactors in the names of your siblings


# SET COMPREHENSION

# Example
# Creating a new set of squared values
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = {x**2 for x in numbers}
# print(squared_numbers)

#  Assignment

# Filtering elements in a list
# numbers = [1, 2, 3, 4, 5]
# even_numbers =  {x for x in numbers if x % 2 == 0}
# print(even_numbers)

# Using a Set Comprehension with strings
# words = ['apple', 'banana', 'Pineapple'] 
# vowels = {'a', 'e', 'i', 'o', 'u'} 
# vowel_words = {word for word in words if any(letter in vowels for letter in word)} 
# print(vowel_words)

# Example
# numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
# unique_numbers = {x for x in numbers}
# print(unique_numbers)

# Generator Comprehension 

# Example
# squares_generator = (x*x for x in range(1,6))
# # print(squares_generator)
# print(list(squares_generator))

#  Example
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
unique_numbers_generator = {x for x in numbers}
print(set(unique_numbers_generator))