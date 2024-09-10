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
    
    def show(self):
        print(self.number)
        print(self.balance)
def main():
    alice = Account("0001", 10000.50, "bsu")
    bob = Account("0002", 100, "iu")
    alice.deposit(-100, "bsu")
    bob.show()
    alice.show()
main()