class Person:
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge
    def sleep(self):
        print("Sleeping")
    def wakeup(self):
        print("Waking up")
    def walk(self):
        print("Walking")
    def talk(self):
        print("Talking")

Pascal = Person("Pascal", 100)
Pascal.sleep()
Pascal.wakeup()
Pascal.walk()
