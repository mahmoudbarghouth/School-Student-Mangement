class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []
    def add_courses(self,cours_name,degree):
        self.courses.append({"course":cours_name,"degree":degree})
