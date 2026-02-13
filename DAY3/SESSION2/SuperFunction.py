class Parent: 
    def __init__(self):
        print("Parent Constructor") 
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child construtor")
# MAIN
obj=Child()
