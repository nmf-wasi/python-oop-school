import random
from school import *


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def evaluateExam(self):
        return random.randint(70, 100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.name = name
        self.classroom = classroom  # classroom object
        self.__id = None
        self.marks = {}  # {"eng": 78, "ICT":97}
        self.subject_Grade = {}  # {"eng":"A"}
        self.grade = None  # final grade

    # getter
    @property
    def id(self):
        return self.__id

    # setter
    @id.setter
    def id(self, value):
        self.__id = value

    def calculate_final_grade(self):
        sum = 0

        for grade in self.subject_Grade.values():
            point = School.grade_to_value(grade)
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade='F'
        else:
            gpa = sum / len(self.subject_Grade)
        self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade: {self.grade} with GPA={gpa}\n"
