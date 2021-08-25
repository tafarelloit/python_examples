
class Student:
    #property self.name
    #property self.grades

    #method average
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def updateGrade(self, grade):
        self.grades = grade

    def printStudent(self):
        return(f"{self.name} average grade is {self.average()}")
#create a new student object

#students = [
#    Student("Itamar",[45,67,89,33,66]),
#    Student("Tony",[88,99,78,98,97]),
#    Student("Mrach",[77,88,99,33,22])   
#]

#for st in students:
#    print(st.printStudent())

class Classroom:
    def __init__(self, lecture, teacher):
        self.lecture = lecture
        self.teacher = teacher
        self.students = []

    def studentOnboard(self, student):
        self.students.append(student)

    def listStudents(self):
        for nst in self.students:
            print(nst.name)

    def listStudentsGrade(self):
        for nst in self.students:
            if len(nst.grades) >=0 :
                print(nst.name, nst.grades)

    def isStudentInTheClass(self, stname):
        found = -1
        idx = 0
        for nst in self.students:
            if nst.name==stname:
                found = idx
                break
            idx = idx + 1
        return(found)

    def updateGrades(self, classroomGrades):
        for name, grade in classroomGrades.items():
            idx = self.isStudentInTheClass(name)
            if idx>=0:
                print(f"Student {name} updated")
                self.students[idx].updateGrade(grade)
            else:
                print(f"Student {name} not found")

#initiate classroom
geography = Classroom("Geography","Itamar Tafarello")

#onboard students
geography.studentOnboard(Student("Mary",[]))
geography.studentOnboard(Student("Tony",[]))
geography.studentOnboard(Student("Mike",[]))

#list student
geography.listStudents()

#list grades
geography.listStudentsGrade()

print(geography.isStudentInTheClass("Itamar"))

#Add grades to the class
grades = {
    "Mary":[67,88,99,100,98],
    "Tony":[57,66,99,70,98],
    "Mike":[47,88,95,100,98],
    "Joseph":[67,88,24,55,98]
    }

geography.updateGrades(grades)

geography.listStudentsGrade()