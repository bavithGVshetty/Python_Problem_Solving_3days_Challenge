class Payment:
    def Pay(self,amount):
        print("Paying",amount,"Using Payment Method")

class GooglePay(Payment):
    def Pay(self,amount):
        print("Paying",amount,"Using Google Pay")
class Card(Payment):
    def Pay(self,amount):
        print("Paying",amount,"Using Card")   
class Cash(Payment):
    def Pay(self,amount):
        print("Paying",amount,"Using Cash")

# Polymorphism
def makePayment(payment_method,amount):
    payment_method.pay(amount)

#MAIN()
amount=int(input("Enter the amount to pay"))

print("Choose Payment Method")
print("1.GooglePay")
print("2.Card")
print("3.Cash")

choice =int(input("Enter choice"))

if choice==1:
    p=GooglePay()
if choice==2:
    p=Card()
if choice==3:
    p=Cash()
else:
    print("Invalid choice")
    exit()

makePayment(p,amount)