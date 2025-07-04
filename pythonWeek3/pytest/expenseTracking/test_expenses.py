import pytest
from expense import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

@pytest.mark.parametrize("amount, expected", [(60.99, 60.99), (100, 100)])
def test_add(tracker, amount, expected):
    tracker.addExpense(amount)
    assert tracker.expenses[0] == expected

@pytest.mark.parametrize("amounts, total", [([100, 50, 49.99], 199.99), ([9.99, 10], 19.99)])
def test_total(tracker, amounts, total):
    for amount in amounts:
        tracker.addExpense(amount)
    assert tracker.total() == pytest.approx(total)

def test_negative_expense(tracker):
    with pytest.raises(ValueError):
        tracker.addExpense(-50)

def test_non_number(tracker):
    with pytest.raises(TypeError):
        tracker.addExpense("Andrew")