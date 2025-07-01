class Classroom:
    def __init__(self, name):
        self.name=name
        self.students=[] #list of student objects
        self.subjects=[] #life of subject objects
    def add_student(self,student):
        self.students.append(student)
        roll_no=f"{self.name}-{len(self.students)+1}" #8-1, 8-2
        student.id=roll_no

    def add_subject(self, subject):
        self.subjects.append(subject)
    def take_semester_final_exam(self):
        for sub in self.subjects:
            sub.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()