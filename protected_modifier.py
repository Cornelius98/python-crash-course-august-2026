class Vehicle:
    def _switchOn(self):
        print("Switched on engine")

    def switchOff(self):
        print("Switched off engine")

    def _drive(self):
        print("Driving on engine")

    def brake(self):
        print("Braking on engine")

    def _start(self):
        self._switchOn()
        self._drive()

#ferrari = Vehicle()
#ferrari.start()

class Benz(Vehicle):
    def selfDrivingMode(self):
        self._start()

C20 = Benz()
C20.selfDrivingMode()