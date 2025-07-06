import pytest
from expense_tracker import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense(tracker):
    tracker.add_expense(100, "food")
    assert tracker.get_total() == 100
    assert tracker.get_category_total("food") == 100
    assert tracker.categories() == ['food']

def test_add_multiple_values(tracker):
    tracker.add_expense(100, "food")
    tracker.add_expense(50, 'car')
    tracker.add_expense(100, 'food')

    assert tracker.get_total() == 250
    assert tracker.get_category_total('food') == 200
    assert tracker.get_category_total('car') == 50
    assert set(tracker.categories()) == {"food", "car"}

def test_unknown_category_total(tracker):
    assert tracker.get_category_total("Nonexistent") == 0