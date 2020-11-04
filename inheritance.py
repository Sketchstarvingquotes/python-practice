#multiple inheritance
class teacher:
    def Teacher_method(self):
        print("Hello from teacher")


class student: 
    def student_method(self):
        print("Hello from student")

class school(teacher, student):
    def school_method(self):
        print("welcome to school")

obj = school()
obj.school_method()
obj.Teacher_method()
obj.student_method()