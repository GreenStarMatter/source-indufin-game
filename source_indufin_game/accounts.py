# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:59:45 2022

@author: Kyle Stanley
"""

class MoneyAccount():
    """This class is intended to hold all of the monetary information
    pertaining to an account.  It contains meta-information to identify
    who owns the account and a name which distinguishes the account.  These
    two meta-labels should be used to distinguish a unique account.  The
    account also includes its current balance.

    balance: How much money is in the account.
    owner: Who owns this account.
    account_name: Name of the account, in the case that an owner has
        muliple accounts.
    """


    def __init__(
            self,
            balance = 0,
            owner = "None Assigned",
            account_name  = "None Assigned"
            ):

        """Inits the class with a balance, owner, and account name."""

        self.balance = balance
        self.owner = owner
        self.account_name = account_name

    def __repr__(self):
        """The representation of the object so that it can be used as an
        abstract entity"""

        return f"money_account({self.balance}, {self.owner}, " + \
            "{self.account_name})"


    def __str__(self):
        """The representation of the object so that it can understood
        as a representation"""

        return f"The account {self.account_name} of {self.owner}" +\
            f" has been a balance of: {self.balance:,}"


    def __add__(self, amount):
        """Allows the ability to quickly access the balance amount and perform
        addition arithmatic"""

        new_amount = self.balance + amount
        return new_amount


    def __sub__(self, amount):
        """Allows the ability to quickly access the balance amount and perform
        subtraction arithmatic"""

        new_amount = self.balance - amount
        return new_amount

    def __iadd__(self, new_amount):
        """Allows the ability to quickly access the balance amount and perform
        in-place addition arithmatic and store the result back into the
        balance"""

        self.balance += new_amount
        return self


    def __isub__(self, new_amount):
        """Allows the ability to quickly access the balance amount and perform
        in-place subtraction arithmatic and store the result back into the
        balance"""

        self.balance -= new_amount
        return self


    def set_balance(self, new_balance, modifier = ""):
        """Allows the ability to manually set the balance amount"""

        self.balance = new_balance * (1000 ** len(modifier))
        print(f"The account {self.account_name} of {self.owner}" +
              f" has been changed to: {self.balance}")


    def set_owner(self, new_owner):
        """Allows the ability to manually set the account owner"""

        old_owner = self.owner
        self.owner = new_owner
        print(f"The account {self.account_name} has been transferred from" +
              f" {old_owner} to {self.owner}")


    def set_account_name(self, new_account_name):
        """Allows the ability to manually set the account name"""

        old_account_name = self.account_name
        self.account_name = new_account_name
        print(f"The owner {self.owner}'s account {old_account_name} has" +
              f" been renamed to {self.account_name}")


    def remove_expense_amount(self, amount, modifier = ""):
        """Allows for modifier on in-place subtract by thousand increments"""

        self.__isub__(amount * (1000 ** len(modifier)))


    def add_deposit_amount(self, amount, modifier = ""):
        """Allows for modifier on in-place addition by thousand increments"""

        self.__iadd__(amount * (1000 ** len(modifier)))
