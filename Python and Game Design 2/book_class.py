class Book:
    def __init__(self, title, color, author, year):
        self.title = title
        self.color = color
        self.author = author
        self.year = year

    # Defining a method to store info of a book
    def book_info(self):
        return f"{self.title} by {self.author} in the year {self.year}"

# Creating a variable to store info of a book 
book1 = Book("Cockcrow", "white", "Lawrence Darmani & John Sackey", 2014)

# Access the method
print(book1.book_info())