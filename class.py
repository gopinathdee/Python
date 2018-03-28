students = []

class Students:
   def add_student(self,name,student_id):
       student = {"student_name":name ,"student_id":student_id }
       students.append(student)

student = Students()
student.add_student("Atheena",100)

print(students)