#Inheritance
class Atria:
    def placement(self):
        print("100% placement")

class Students(Atria):
    def play(self):
        print("Playing ko-ko")

class Bike(Students):
    def ride(self):
        print("START")
