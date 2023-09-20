class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!!welcome to the Deposit & withdraw machine")
    def deposit(self):
        amount=float(input("Enter amount to be deposited:"))
        self.balance+=amount
        print("\amount deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter the amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n you withdraw amount:",amount)
        else:
            print("\n insufficiant balance")
    def display(self):
        print("\n net available balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
