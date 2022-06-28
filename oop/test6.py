

from datetime import MAXYEAR


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Account owner: {self.owner}")        
        print(f"Account balance: {self.balance}")
    
    def deposit(self,dep):
        self.dep = dep
        self.balance += self.dep
        print("Deposit Accepted")
        
    def withdraw(self, withd):
        self.withd = withd
        if(self.balance <= self.withd):
            print("Funds Unavalable!")
        else:
            self.balance -= self.withd
            print("withdrawal Accepted")  
            
    def __str__(self):
        return f"The owner: {self.owner} \nBalnce: {self.balance}" 
    
     


myacct = Account("jose", 100)

print(myacct.owner)

print(myacct.balance)

myacct.deposit(50) 
print(myacct.balance)
myacct.withdraw(75)
print(myacct.balance)
myacct.withdraw(500)

print(myacct)



