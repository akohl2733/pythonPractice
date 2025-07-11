from modules import Expense

car_payments = Expense()

car_payments.addExpense("Tires", 800.00)
car_payments.addExpense("Oil", 99.99)

print(car_payments.get_expenses())