import unittest
from bankaccount import BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()
    def test_Deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)
    def test_Withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    def test_Overdraw(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == '__main__':
    unittest.main()