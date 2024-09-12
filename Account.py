class Account():
    def __init__(self, n, b, p):
        self.number = n
        self.balance = b
        self.password = p 
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None
        self.balance += amountToDeposit
        return self.balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect password")
            return None
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than your balance")
            return None
        self.balance -= amountToWithdraw
        return self.balance
    
    def show(self):
        print(self.number)
        print(self.balance)
def main():
    alice = Account("0001", 10000.50, "bsu")
    bob = Account("0002", 100, "iu")
    bob.withdraw(50, "iu")
    bob.show()
    alice.show()
main()