class Animal:
    def sound(self):
        return "Generate animal sound"
    
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    def wag_tail(self):
        return "Tail wagging"
    
animal = Animal()
dog = Dog()

print(animal.sound())
print(dog.sound())
print(dog.wag_tail())