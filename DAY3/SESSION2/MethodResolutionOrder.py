class A:
    def show(self):
        print("Showing A")
class B:
    def show(self):
        print("Showing B")
class C(A,B):
    pass
# MAIN()
obj=C()
obj.show()
