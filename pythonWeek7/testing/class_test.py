class BankAccount:

    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        self.balance -= amount

import pytest

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw(account):
    account.withdraw(60)
    assert account.balance == 40

def test_withdraw_too_much(account):
    with pytest.raises(ValueError):
        account.withdraw(200)