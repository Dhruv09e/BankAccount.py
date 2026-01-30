class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance = balance
   
    def deposit(self,amount):
        self.__balance += amount
        print("Amount Deposited")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn")
        else:
            print("Amount unavailable")

    def get_balance(self):
        return self.__balance       

class SavingsAccount(Bankaccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            super().withdraw(amount)
        else:
            print("Not Enough Balance in Savings Account ")

acc1=Bankaccount("Rahul",5000)
acc2=SavingsAccount("Raj",10000)

acc1.deposit(1000)
acc1.withdraw(2000)
print(acc1.get_balance())

acc2.deposit(5000)
print(acc2.get_balance())
        
    
