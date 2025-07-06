from typing import Dict, List

class ExpenseTracker:

    def __init__(self):
        self.expenses: Dict[str, List[int]] = {}

    def add_expense(self, amount: int, category: str) -> None:
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)
    
    def get_total(self) -> int:
        return sum(sum(val) for val in self.expenses.values())
    
    def get_category_total(self, category: str) -> int:
        return sum(self.expenses.get(category, []))

    def categories(self) -> List[str]:
        return list(self.expenses.keys())