# open() to open a file
# read() r to read a file
# write() to write into a file
# close() to close a file

# Reading from a file
with open('input.txt', 'r') as f:
    data = f.read()

# Writing into another file
with open('output', 'w') as f:
    f.write(data)