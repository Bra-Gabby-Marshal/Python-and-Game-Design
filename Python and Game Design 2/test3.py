# Defining a class
class Car:
    def __init__(self, make, model, year):
        self.make = make # Attribute: make of the car
        self.model = model # Attribute: model of the car
        self.year= year # Attribute: year of manufacturing


    # Getting the description of the car
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
    # Method to start the car
    def start(self):
        return "Car Started!"
    
    # Method to stop the car
    def stop(self):
        return "Car Stopped!"
    
# Creating a variable to store data about the Car class
my_car = Car("Toyota", "High Lander", 2023)

# Accesing values 
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)

# Using Method
# print(my_car.get_description())
# print(my_car.start())
print(my_car.stop())