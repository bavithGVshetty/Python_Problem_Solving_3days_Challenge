# Compile-time poly

class Atria:
    def add(self,*args):
        total =0
        for i in args:
            total+=i
        print(total)

obj=Atria()
obj.add(10,10,10.0)