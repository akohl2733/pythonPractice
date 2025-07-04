import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        print("Setting up bank account...")
        self.acct = BankAccount("Andrew", 100)

    def tearDown(self):
        print("Removing bank account...")
        del self.acct

    def test_deposit(self):
        self.acct.deposit(50)
        self.assertEqual((self.acct.balance), 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.acct.deposit(-50)

    def test_withdraw(self):
        self.acct.withdraw(100)
        self.assertEqual((self.acct.balance), 0)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.acct.withdraw(1000)


if __name__ == "__main__":
    unittest.main()