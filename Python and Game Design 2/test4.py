class Animal:
    def __init__(self, name):
        self.name = name

    def s(self):
        raise NotImplementedError("Subclass must implement an abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
    
# Variables
dog = Dog("Berry")
cat = Cat("Rainbow")

# Accessing data
print(dog.speak())
print(cat.speak())
