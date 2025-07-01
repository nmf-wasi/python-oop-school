from school import School
from person import Teacher
class Subject:
    def __init__(self, name, teacher,max_marks):
        self.name=name
        self.teacher=teacher  #object of teacher
        self.max_marks=max_marks
        self.pass_marks=60
    
    def exam(self, students): #list of students
        for student in students:
            mark=self.teacher.evaluateExam()
            student.marks[self.name]=mark
            student.subject_Grade[self.name]= School.calculate_grade((mark))