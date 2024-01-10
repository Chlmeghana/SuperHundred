class BankAccount:
    def __init__(self, name, accno, balance=0):
        self.name = name
        self.accno = accno
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient money.")
        else:
            self.balance -= amount

    def display(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.accno}")
        print(f"Current Balance: {self.balance}") 
class SBI(BankAccount): 
    def __init__(self,name,accno,balance=0): 
        self.name=name
        self.accno=accno 
        self.balance=balance
    

my_account = BankAccount("Meghana", "1234567890")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.display()
sbi_account=SBI("Lakshmi","87654321") 
sbi_account.deposit(8000) 
sbi_account.withdraw(800) 
sbi_account.display()
