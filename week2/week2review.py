## Expense Tracker Utility

from functools import wraps
import time
print("[LOG] - At top")
# Use custom context manager
class SafeFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, x, y, z):
        self.file.close()

print("[LOG] - Above Custom Error")
# Custom errors
class NegativeAmountError(Exception):
    pass
class EmptyStringError(Exception):
    pass


def log_time(func):
    print("[LOG] - Decorator")
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[TIME] - this function took {end_time - start_time:.4f} seconds.")
        return res
    return wrapper


expenses = []
# Add expenses and validating inputs
@log_time
def addExpenses():
    print("[LOG] - This happened")
    while True:

        # Analyze decription parameter
        description = input("What did you pay for?\n")
        try:
            if not description.strip():
                raise EmptyStringError("Please enter a description")
        except EmptyStringError as e:
            print(f"Error {e}")
            continue

        # Analyze amount
        amount_str = input("How much did it cost?")
        amount_cleaned = amount_str.strip('$').replace(",", ".")
        try:
            amount = float(amount_cleaned)
            if amount <= 0:
                raise NegativeAmountError("Please only enter numbers above zero.")
            expenses.append({"Description": description, "Amount": amount})
        except ValueError:
            print("Please only enter a valid number")
            continue
        except NegativeAmountError as e:
            print(f"Error {e}")
            continue
        
        ans = input("Do you want to add another purchase? [y/n]\n").lower()
        if ans != 'y':
            break

addExpenses()

# save to a file (expenses.txt)
with SafeFile("expenses.txt", 'w') as f:
    for expense in expenses:
        f.write(f'Description: {expense["Description"]} -- Amount: {expense["Amount"]:.2f}\n')

# view all expenses
with SafeFile('expenses.txt', 'r') as f:
    lines = f.readlines()
    print("All expenses:")
    for line in lines:
        print(line.strip())