class Subject:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        
        
        
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        return self.marks

    def calc_average(self):
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)
            
            
            
            
import subject_module
import student_module

math = subject_module.Subject("Math", "Ahmed")
english = subject_module.Subject("English", "Mohammed")
science = subject_module.Subject("Science", "Ali")


student1 = student_module.Student("Alaa", 18, "Gaza")
student2 = student_module.Student("Asmaa", 17," Khan Younes")
student3 = student_module.Student("Nada", 16, "Rafah")