from budget.expenses import add_expense
from budget.income import add_income
from budget.summary import summary
import re

balance = 0

while True:

    try:
        str_amount = re.sub(r'[.,$]', '', input("How much income did you make?").strip())
        amount = float(str_amount)
        balance = add_income(balance, amount)

        str_expense = re.sub(r'[.,$]', '', input("How many expenses did you pay?").strip())
        expenses = float(str_expense)
        balance = add_expense(balance, expenses)
        
    except ValueError:
        print("Please only use numbers")

    print(f"${summary(balance)}")

    again = input("Would you like to add further income/expenses? [y/n]").strip().lower()
    if again != 'y':
        break

print(f'Final balance: ${balance:.2f}')