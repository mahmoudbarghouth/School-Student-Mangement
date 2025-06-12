from Studentclass import *



class Schoolclass():
    def __init__(self):
        self.students = []

    def addStudent(self,student):
        self.students.append(student)

    def removeStudent(self,student):
        self.students.remove(student)
    def printStudents(self):
        for student in self.students:
            print(f'student name is : {student.name}')
            for cours in student.courses:
                print(f" Course: {cours['course']} - Degree: {cours['degree']}")


school=Schoolclass()
student1=Student("ahmed")
student1.add_courses('math',88)
student1.add_courses('science',95)
student2=Student("ali")
student2.add_courses('math',90)
student3=Student("heba")
student3.add_courses('math',95)
school.addStudent(student1)
school.addStudent(student2)
school.addStudent(student3)
school.printStudents()
school.removeStudent(student2)
school.printStudents()

