#Polymorphism - method overloading
class Calculator:
    def add(self, a =0, b=0, c=0):
        sum = a + b + c
        print("Sum is: ", sum)


Calculator = Calculator()
Calculator.add(10)
Calculator.add(20, 30)
Calculator.add(30, 40, 50)