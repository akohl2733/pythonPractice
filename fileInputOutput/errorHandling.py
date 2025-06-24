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