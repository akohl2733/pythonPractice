class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def addExpense(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Expense must be a number.")
        if amount < 0:
            raise ValueError("Expense cannot be negative.")
        self.expenses.append(amount)

    def total(self):
        return round(sum(self.expenses), 2)