class BankAccount:

    def __init__(self, balance: float = 0):
        self.balance = balance
    
    def withdraw(self, amt: float):
        if amt > self.balance:
            raise ValueError("ERROR: insufficient funds")
        self.balance -= amt
        return f"Successful withdrawal. Your current balance is now {self.balance}"
    
    def deposit(self, amt: float):
        self.balance += amt
        print(f"Successful deposit. Your current balance is now {self.balance}")

    def __repr__(self):
        return f"SavingsAccount(balance={self.balance})"

    def __str__(self):
        return f"Balance: {self.balance}"

class SavingsAccount(BankAccount):

    def __init__(self, balance: float = 0, percent_rate: float = 0):    # rate should be in percent format
        super().__init__(balance)
        self.percent_rate = percent_rate

    def compound_interest(self, times_compounded: int, years: int) -> float:
        return self.balance * ((1 + (self.percent_rate / 100) / times_compounded) ** (years * times_compounded))

    def __repr__(self):
        return f"SavingsAccount(balance={self.balance}, rate={self.rate})"

    def __str__(self):
        return f"Balance: {self.balance}, Interest Rate: {self.rate}%"

my_acct = SavingsAccount(1000, 5)
my_acct.withdraw(500)
my_acct.deposit(500)
print(my_acct.compound_interest(12, 10))
print(my_acct)
