class Parent:
    def show(self):
        print("Parent Method")
class Child(Parent):
    def show(self):#Overriding
        print("Child Method")

obj=Child()
obj.show()