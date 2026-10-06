#Polymorphism - method overriding
class Universal:
    def dispense(self):
        print("Universal dispense method ...")

class Health(Universal):
    def dispense(self):
        print("Dispense medicine ...")

class Accounts(Universal):
    def dispense(self):
        print("Dispense withdraws ...")

class Game(Universal):
    def dispense(self):
        print("Dispense bullets ...")

#Health object
Health = Health()
Health.dispense()

#Accounts object
Accounts = Accounts()
Accounts.dispense()

#Game object
Game = Game()
Game.dispense()