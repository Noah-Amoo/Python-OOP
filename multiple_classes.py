class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)

student01 = Student('Afriyie', 30, 97)
student02 = Student('Yaw', 25, 93)
student03 = Student('Nana', 35, 98)

#   Adding student(s) to a course
coding = Course('Coding', 2)
coding.add_student(student01)
coding.add_student(student02)
print(coding.add_student(student03))

print(coding.get_average_grade())