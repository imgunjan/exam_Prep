"""
In this example, we create a BankAccount object, deposit some money, check the balance, and try to withdraw more than the available balance. The private __balance attribute is not directly accessible outside the class, ensuring that the account's balance is properly encapsulated and protected.
"""


class BankAccount:
    def __init__(self, account_number, bank_balance):
        self.account_number = account_number
        self.__bank_balance = bank_balance  # private Attribute

    def deposit(self, amount):
        self.__bank_balance += amount

    def withdraw(self, amount):
        if self.__bank_balance > amount:
            self.__bank_balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        return self.__bank_balance


account = BankAccount("123456789", 1000)

account.deposit(1000)
account.withdraw(500)
account.withdraw(10000)
