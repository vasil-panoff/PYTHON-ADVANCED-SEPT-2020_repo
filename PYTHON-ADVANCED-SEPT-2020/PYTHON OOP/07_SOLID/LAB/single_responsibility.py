#Every CLass Take only one responsibility

class Student:
    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name


class StudentRegistry:
    def __init__(self):
        self.students = []

    def register(self, student: Student):
        self.students.append(student)

    def unregister(self, student: Student):
        self.students.pop(self.students.find(student))

    def find_student_by_name(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student

student = Student('Vasil')
registry = StudentRegistry()
print(student.name)