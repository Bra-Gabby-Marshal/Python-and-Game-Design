class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade= grade


    def promote(self):
        self.grade += 1

# Creating a variable of a student
student1 = Student("Daniel", 13, 9)
student2 = Student("Aarnick", 10, 10)
student3 = Student("Lios Donkor", 12, 6)

# print(student2.grade)
student1.promote()
print(student1.grade)
