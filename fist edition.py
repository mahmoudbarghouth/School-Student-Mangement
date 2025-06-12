class Student:
    def __init__(self,name):
        self.name = name

class Courses:
    def __init__(self,student,course,degree):
        student.course = course
        student.degree = degree




class Schoolclass():
    def __init__(self):
        self.students = []
        self.courses = []
    def addStudent(self,student):
        self.students.append(student)
    def addCourse(self,course):
        self.courses.append(course)
    def removeStudent(self,student):
        self.students.remove(student)
    def printStudents(self):
        for student in self.students:

                print(f"student name is : {student.name} his  {student.course} degree is:{student.degree}")

student1=Student("ahmed")
cours1=Courses(student1,"math",88)
student2=Student("ali")
cours2=Courses(student2,"math",90)
student3=Student("heba")
cours3=Courses(student3,"math",95)
school=Schoolclass()
school.addStudent(student1)
school.addStudent(student2)
school.addStudent(student3)
school.addCourse(cours1)
school.addCourse(cours2)
school.addCourse(cours3)
school.printStudents()
school.removeStudent(student1)
school.printStudents()

