class Student:
    def printName(self):
        print("Student Name: Guido Van Rossum")

    def printStudentNumber(self):
        print("Student Number: 12345")

    def printStudentDetails(self):
        self.printName()
        self.printStudentNumber()

#Calling public method from with class
Guido = Student()
Guido.printStudentDetails()

#Calling public method from object
Van = Student()
Van.printName()
Van.printStudentNumber()


#Inheriting public methods
class Lecturer(Student):
    pass

Steven = Lecturer()
Steven.printName()