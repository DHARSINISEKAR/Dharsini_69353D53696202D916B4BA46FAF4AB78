class student:
   def __init__(self,name,roll_number,cgpa):
     self.name=name
     self.roll_number=roll_number
     self.cpga=cgpa
   def sort_studens(students_list):
     sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
     return sorted_student
student=[student("Hari","A123",7.9),student("Srikanth","A124",9.8),student("Sowmya","A125",8.9),student("Mahi","A126",9.2)]
sorted_students=sorted_students(students)
for student in sorted_students:
    print("Name:{},Roll Number:{},cgpa:{}",format(student.name,student.roll_number,student.cpga))
                                            
