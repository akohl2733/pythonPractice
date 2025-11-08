class Calculator:

    def __init__(self, amount=0):
        self.amount = amount

    def add(self, num):
        self.amount += num
        return self.amount

    def subtract(self, num):
        self.amount -= num
        return self.amount

    def multiply(self, num):
        self.amount *= num
        return self.amount

    def divide(self, num):
        if num == 0:
            raise ZeroDivisionError
        self.amount /= num
        return self.amount

    def __str__(self):
        return f"The Calculator is showing {self.amount}"