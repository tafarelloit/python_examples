"""
This example is tighted coupled means it has hard coded
Which is bad in the design
"""
#my_student = {
#    "name":"Itamar",
#    "grades":[70,88,96,55]
#}

#def average_grade(student):
#    return sum(student["grades"]) / len(student["grades"])

#print(average_grade(my_student))



"""
could we add a function in the dictionary to eliminate the hard code
"""
#my_student = {
#    "name":"Itamar",
#    "grades":[70,88,96,55]
#    "average": would make sense to put a function to calculate
#               but it doesn't work
#}

#def average_grade(student):
#    return sum(student["grades"]) / len(student["grades"])

#print(average_grade(my_student))


"""
How to fix using a class
"""
class Student:
    #property self.name
    #property self.grades

    #method average
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def printStudent(self):
        return(f"{self.name} average grade is {self.average()}")
#create a new student object

students = [
    Student("Itamar",[45,67,89,33,66]),
    Student("Tony",[88,99,78,98,97]),
    Student("Mrach",[77,88,99,33,22])   
]

for st in students:
    print(st.printStudent())
