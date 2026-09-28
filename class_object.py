class Person():
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)


#Class Object
christine = Person("Cornelius", 100)
christine.printName()
christine.printAge()