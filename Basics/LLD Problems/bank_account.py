"""
Design Bank Account Class
Problem: Create a BankAccount class that manages a simple bank account with deposit, withdrawal, and balance checking functionality.

Requirements:

Fields: accountNumber, ownerName, balance
Constructor that initializes the account with owner name and account number (balance starts at 0)
deposit(amount): adds money to balance (only positive amounts)
withdraw(amount): removes money if sufficient balance exists, returns success/failure
getBalance(): returns current balance
"""

from typing import List
class BankAccount:
    def __init__(self,accountNumber,ownerName="UserXYZ",balance=0):
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self,amount:float) -> None:
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
        
    def withdraw(self,amount) -> bool:
        if amount > 0 and self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def getBalance(self)-> float:
        return self.balance

if __name__ == "__main__":
    acc1 = BankAccount(12345,"Mohd Waqas",1500)
    print(acc1.accountNumber)
    print(acc1.ownerName)
    print(acc1.balance)
    acc1.deposit(50)
    res = acc1.getBalance()
    print("Balance after deposit -----")
    print(res)
    print()
    print("Balance after withdraw -----")
    acc1.withdraw(670)
    res = acc1.getBalance()
    print(res)