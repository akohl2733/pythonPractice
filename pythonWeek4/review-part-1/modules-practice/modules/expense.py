from typing import Dict, Union
class Expense:

    def __init__(self):
        self.expenses = {}

    def addExpense(self, item: str, amount: Union[int, float]) -> Union[Dict[str, float] | str]:
        if isinstance(amount, (float, int)):
            self.expenses[item] = float(amount)
            return {item: float(amount)}
        return "Please enter a valid amount"
    
    def get_expenses(self) -> Dict[str, float]:
        return self.expenses