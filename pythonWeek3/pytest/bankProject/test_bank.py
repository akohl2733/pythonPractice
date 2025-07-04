import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("Andrew", 100)

@pytest.mark.parametrize("amount, expected", [(50, 150), (0, 100)])
def test_deposit(account, amount, expected):
    account.deposit(amount)
    assert account.balance == expected

def test_withdraw(account):
    account.withdraw(100)
    assert account.balance == 0

def negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-50)

def insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(1000)

def test_default_balance():
    a = BankAccount("Alex")
    assert a.balance == 0