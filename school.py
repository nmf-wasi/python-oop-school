class School:
    def __init__(self, name, address):
        self.name=name
        self.address=address
        self.teachers={} #{"sebject":"teacherName"}
        self.classrooms={} #{"eight":classroom_object}
        

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject]=teacher    
    def student_admission(self,student):
        pass

    @staticmethod #->class's own method, object or instances cant use this func/method
    def calculate_grade(marks):
        if marks>=96 and marks<=100:
            return "A+"
        elif marks>=91 and marks<=95:
            return "A"
        elif marks>=86 and marks<=90:
            return "B+"
        elif marks>=81 and marks<=85:
            return "B"
        elif marks>=76 and marks<=80:
            return "C+"
        elif marks>=71 and marks<=75:
            return "C"
        elif marks>=66 and marks<=70:
            return "D+"
        elif marks>=61 and marks<=66:
            return "D"
        else:
            return "F"
        
    @staticmethod
    def grade_to_value(grade):
        grade_map={
            "A+":4.5,
            "A+":4.0,
            "B+":3.5,
            "B":3.0,
            "C+":2.5,
            "C":2.0,
            "D+":1.5,
            "D":1.0,
            "F":0.0
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        if value>=4.1 and value<=4.5: return "A+"
        elif value>=3.6 and value<=4.0: return "A"
        elif value>=3.1 and value<=3.5: return "B+"
        elif value>=2.6 and value<=3.0: return "B"
        elif value>=2.1 and value<=2.5: return "C+"
        elif value>=1.6 and value<=2.0: return "C"
        elif value>=1.1 and value<=1.5: return "D+"
        elif value>=0.6 and value<=1.0: return "D"
        else: return "F"
    
    def __repr__(self):
        #all clasrooms
        #all students
        #all subject
        #all teachers
        #all student results
        pass
    