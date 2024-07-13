# I/O with Basic FIles in Python

# # Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, world!\nThis is a test file')

# # Read from a file
with open('function2.py', 'r') as file:
    data = file.read()
    print(data)


