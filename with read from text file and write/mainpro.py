


class Student2:
    def __init__(self, name):
        self.name = name
        self.corses = {}
    def addcourses(self,course_name,degree):
       self.corses[course_name] =float(degree)
    def show_data1(self,):
        for i ,j in self.corses.items():
            print(f" {self.name}...{i} - {j}")

class School:
    def __init__(self):
        self.school = []
    def read_data_file(self,filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            headers=lines[0].strip().split(',')[1:]
            for line in lines[1:]:
                parts=line.strip().split(',')
                name=parts[0]
                degrees=parts[1:]
                student=Student2(name)
                student.name=name
                for course_name, grade in zip(headers, degrees):
                    student.addcourses(course_name, grade)
                self.school.append(student)
    def show_all_students(self):
        for student in self.school:
            student.show_data1()
            print("-" * 30)

    def save_successful(self, filename):
        import json
        success = [s.name for s in self.school if all(d >= 50 for d in s.corses.values())]
        with open(filename, "w") as f:
            json.dump(success, f, indent=4)

school = School()
school.read_data_file("grades.txt")
school.show_all_students()
school.save_successful("sucess.txt")


