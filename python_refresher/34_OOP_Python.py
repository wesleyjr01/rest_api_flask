class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (90, 90, 93, 78, 90)

    def avg_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student(name="Dunno")
print(f"Student Name: {student.name}")
print(f"Student Notes Average: {student.avg_grades()}")
