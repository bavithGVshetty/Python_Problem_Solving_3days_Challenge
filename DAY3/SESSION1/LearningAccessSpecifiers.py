#Private,Public Protected
# Python do not have these keywords

class Atria:
    def __init__(self):
        self.name="Darshan" #Public variable
        self.__age=31  #Private 
        self._gender="Male"  #Protected

# MAIN()
a=Atria()
print(a.name)
print(a.__age)