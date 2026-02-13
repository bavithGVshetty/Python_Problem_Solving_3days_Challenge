class BankAccount:
    def __init__(self,name,accn,balance):
        self.name=name
        self.accn=accn
        self.__balance=balance
    def getBalance(self):
        return self.__balance
    def setBalance(self ,balance):
        self.__balance=balance

# main
acc1=BankAccount("BAVI",123,10)
print(acc1.getBalance())
acc1.setBalance(100)
print(acc1.getBalance())