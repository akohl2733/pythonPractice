def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError:
        return "Please only enter valid numbers."
    else:
        return result
    finally:
        print("Executed division attempt")

# print(divide(10, 0))

class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot take square root of a negative number!")
    else:
        return n ** 0.5
    
# try:
#     print(square_root(float(input("What number do you want to take the square root of?\n"))))
# except NegativeNumberError as e:
#     print("caught error:", e)
# except ValueError as type:
#     print("Please enter a valid number")
# finally:
#     print("Square root operation attempted.")

## -----------------------------------------------------
# Budget tracking application

class NonPositiveNumberError(Exception):
    pass


def validAmount(amt):
    if amt <= 0:
        raise NonPositiveNumberError("Not a positive amount.")
    else:
        return amt
    
expenses = []
    
try:
    with open("expenses.txt", "r") as f:
        for line in f:
            desc, amt = line.strip().split(",")
            expenses.append({"Description": desc, "Amount": float(amt)})
except FileNotFoundError as e:
    print("No previous file found - starting fresh")



while True:

    desc = input("Please enter the item you spent money on today:\n")

    try:
        amt = validAmount(float(input(f"Please enter the amount spent (USD) on {desc}\n")))
        expenses.append({"Description": desc, "Amount": amt})
        with open("expenses.txt", "a") as f:
            f.write(f"{desc},{amt}\n")
    except NonPositiveNumberError as pos:
        print("Caught error:", pos)
    except ValueError as val:
        print("Please enter a valid number")
    finally:
        print("Entry attempt finished.")

    more = input("Do you want to add another expense? (y/n)\n").lower()
    if more != 'y':
        break

print("\nFinal Expense List:\n")
for expense in expenses:
    print(f"{expense['Description']}: ${expense['Amount']:.2f}")


## --------------------------------------------------------
# quiz
# Question 1


def product(a, b):
    if 0 in {a,b}:
        print("You are multiplying by zero.")
    try:
        return a*b
    except TypeError as e:
        print("Please only enter numeric values.")
    

# --------------------------------------
# Question 2

class CalorieAmountError(Exception):
    pass

def insert_calories(cal):
    if cal > 10000 or cal < 500:
        raise CalorieAmountError("Please enter a caloric amount over 500 but under 10,000.")
    else:
        return cal
    
# ---------------------------------
# Question 3

daily_goals = []
with open("goals.txt", "r") as f:
    for line in f:
        daily_goals.append(line.strip())



# -----------------------------------------
# Question 4

import csv

expenses = []

while True:
    desc = input("What did you spend money on?\n")
    try:
        amt = float(input("How much did you spend?\n"))
        expenses.append({"Description": desc, "Amount": amt})
    except TypeError as e:
        print("Please enter a valid amount.")
    finally:
        print("Expense Addition Attempted.")
    
    more = input("Do you want to add another expense? (y/n)\n").lower()
    if more != "y":
        break


with open("expenses.csv", 'a', newline="") as csvfile:
    w = csv.writer(csvfile)
    for expense in expenses:
        w.writerow([expense["Description"], expense["Amount"]])