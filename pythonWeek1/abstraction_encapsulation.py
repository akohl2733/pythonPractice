class BankAccount():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f'Deposit Successful. You deposited ${amt}.')
        else:
            print("Deposit was not successful -- Please enter a value above zero.")

    def withdraw(self, amt):
        if amt > self.__balance:
            print(f'Invalid withdrawal amount -- you only have {self.getBalance()} in your account')
        elif amt < 0:
            print("Please enter an amount to withdraw over 0.")
        else:
            self.__balance -= amt
            print("Withdrawal Successful.")

    def getBalance(self):
        return f'Your balance is: ${self.__balance}'
    
    def __str__(self):
        return f'{self.owner}\'s account -- Total Amount: {self.__balance}'
    
    def transfer(self, amount, obj):
        if amount > 0 and obj:
            obj.deposit(amount)
            self.__balance -= amount
            print(f'You successfully deposited {amount} into {obj.owner}\'s account')
        elif amount > self.__balance:
            print("This account does not have the funds for that transfer.")
        else:
            print("Please enter a valid name or amount")
    
myacct = BankAccount("Andrew", 1000)
acct2 = BankAccount("Mike", 500)

# acct2.transfer(20, myacct)
# print(myacct.getBalance())
# print(acct2.getBalance())


# ------------------------------------------------------------------------
## Abstraction


class CoffeeMachine:

    def __init__(self):
        self.__water_level = 100

    def make_coffee(self):
        if self.__water_level >= 20:
            self.__brew()
            self.__water_level -= 20
            return "Here's your coffee!"
        else:
            return "Not enough water!"
        
    def __brew(self):
        print("Brewing......")

    def get_water_level(self):
        return self.__water_level

c = CoffeeMachine()


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):

    def __init__(self):
        pass
    
    def start_engine(self):
        print("Vroom")
    
    def stop_engine(self):
        print(".......")


car = Car()


class Appliances(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliances):

    def turn_on(self):
        print('...whiiiirrrrrRRRRRRR')
    
    def turn_off(self):
        print('WHHHHHIIIIiiiirrrrr....')


class Microwave(Appliances):

    # def __init__(self):           do not have to initialize a class that does not create any variables -- already automatically done my python
    #     pass

    def turn_on(self):
        print('...vrooooOOOMMMMM')
    
    def turn_off(self):
        print('VROOOoooommmm....')