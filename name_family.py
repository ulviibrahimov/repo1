class Student:
    courseMarks={}
    name=""
    def __init__(self,name,family):
        self.name=name
        
    def addCourseMark (self,course,mark):
        self.courseMarks[course]=mark
        
    def average(self):
        return sum(courseMarks)/len(courseMarks)
    