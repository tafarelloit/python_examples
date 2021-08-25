class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

#    def weekly_salary(self):
#        return self.salary * 44
    @property
    def weekly_salary(self):
        return self.salary * 44

ralf = WorkingStudent("Ralf", "MIT", 19)
print(ralf.salary)
#print(ralf.weekly_salary())
print(ralf.weekly_salary)