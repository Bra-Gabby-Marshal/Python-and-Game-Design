class Student:
    def __init__(self, name, age, class_level):
        self.name = name
        self.age = age
        self.class_level = class_level

class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def get_student_by_name(self, name):
        return self.students.get(name)

student_db = StudentDatabase()
student_db.add_student(Student("Daniel", 13, "Basic 8"))
student_db.add_student(Student("Aarnick", 10, "Basic 4"))
student_db.add_student(Student("Lios", 12, "Basic 4"))

print(student_db.get_student_by_name("Daniel").age)
