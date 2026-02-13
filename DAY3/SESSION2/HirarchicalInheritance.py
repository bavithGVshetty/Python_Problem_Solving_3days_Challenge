class GrandFather:
    def hobby(self):
        print("Hunting")
class Father(GrandFather):
    def hobby(self):
        print("Riding")
class Child(GrandFather):
    def hobby(self):
        print("Sleeping")
