class Mobile:
    # Mobile(){
    def __init__(self):
        pass
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    #Function in python
    def display(self):
        print("Brand",self.brand)
        print("Model",self.model)
        print("Price",self.price)

# MAIN
m1=Mobile("Samsung","S24",75000)
m1.display()
