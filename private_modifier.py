class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __talk(self):
        print("Private talk method")

    def chat(self):
        print("Public chat method, that invokes private talk method")
        self.__talk()

Rosum = Person("Rosumm", 100)
Rosum.chat()