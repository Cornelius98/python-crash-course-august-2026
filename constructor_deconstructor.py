class Person:
    def __init__(self, name, age):
        print("Constructor running..")
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

    def __del__(self):
        print("Destructor running..")

Pascal = Person("Pascal", 20)