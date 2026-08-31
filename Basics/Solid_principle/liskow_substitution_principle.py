"""
Definition: It states that objects of a parent class should be replaceble with objects of a child class without breaking the program

Simple terms:
 - if child class is-a Parent class, then child should work exactly like Parent
 - you should be able to use Child class wherever Parent class is expected
 - Child class should not break the behavior that Parent class promises

No class should be forced to implement methods it does not use.
Split large interfaces into smaller, more specific ones.
"""

###### BAD EXAMPLE #######

from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,balance: int):
        self.balance = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("Can't withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, remaining balance {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self,amount):
        raise Exception("Can't withdraw from FD")
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")


# s = SavingsAccount(1000)
# s.deposit(1000)
# s.withdraw(1500)

# fd = FixedDepositAccount(1000)
# fd.deposit(1000)
# fd.withdraw(500)




#########33 GOOD EXAMPLE #############3

class Account(ABC):
    def __init__(self,balance):
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass


class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingAccount(WithdrawableAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Can't withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, current balance {self.balance}")

class FixedDepositAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited successfully, balance {self.balance}")


# s = SavingsAccount(1000)
# s.deposit(500)
# s.withdraw(1000)

fd = FixedDepositAccount(1000)
fd.deposit(500)
        

