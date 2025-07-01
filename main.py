from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school=School("Sejong", "Seoul")


# adding class room
eight=Classroom("Eight")
nine=Classroom("Nine")
ten=Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#adding student
wasi=Student("NMF Wasi", eight)
kel=Student("Kel", eight)
joyce=Student("Joyce", eight)
yuna=Student("Yuna", nine)
lia=Student("Lia", nine)
chaer=Student("Chaer", ten)

school.student_admission(wasi)
school.student_admission(kel)
school.student_admission(joyce)
school.student_admission(yuna)
school.student_admission(lia)
school.student_admission(chaer)


#adding teachers
yeji=Teacher("Yeji")
ryu=Teacher("Ryu")
xu=Teacher("XU")
swn=Teacher("Sowon")


# adding sub 
dsa=Subject("Data Structure and Algo",yeji)
intro_to_dataScience=Subject("Intro to Data Science",yeji)
python=Subject("Python",ryu)
cyberSec=Subject("Cyber Security",ryu)
korean=Subject("Korean Language",xu)
physics=Subject("Physics",swn)


eight.add_subject(korean)
eight.add_subject(physics)
nine.add_subject(dsa)
nine.add_subject(python)
ten.add_subject(cyberSec)
ten.add_subject(intro_to_dataScience)


eight.take_semester_final_exam()
print(school)