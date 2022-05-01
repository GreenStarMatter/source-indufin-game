# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:43:51 2022

@author: Kyle Stanley


This tests the core accounting logic.  This will be the storage of money
and the ability to create simple changes to those balances.
"""


from source_indufin_game import accounts


def test_account_object_shape():
    """Tests basics of account creation"""

    basic_account = accounts.MoneyAccount()
    assert basic_account
    assert basic_account.balance == 0
    assert basic_account.owner == "None Assigned"
    assert basic_account.account_name == "None Assigned"

    basic_account = accounts.MoneyAccount(100, "Player 1", "Acct 1")
    assert basic_account.balance == 100
    assert basic_account.owner == "Player 1"
    assert basic_account.account_name == "Acct 1"


def test_account_altering_properties():
    """Tests property setting functions of account class"""

    changing_account = accounts.MoneyAccount()
    changing_account.set_balance(100)
    assert changing_account.balance == 100

    changing_account.set_balance(100,"X")
    assert changing_account.balance == 100000

    changing_account.set_owner("Player 1")
    assert changing_account.owner == "Player 1"

    changing_account.set_account_name("Acct 1")
    assert changing_account.account_name == "Acct 1"


def test_account_amount_properties():
    """Tests balance changing logic of account class"""

    changing_account = accounts.MoneyAccount()
    changing_account.set_balance(100)
    assert changing_account.balance == 100

    changing_account.remove_expense_amount(100)
    assert changing_account.balance == 0

    changing_account.add_deposit_amount(100)
    assert changing_account.balance == 100
    assert changing_account-100 == 0
    assert changing_account+100 == 200

    changing_account+=100
    assert changing_account.balance == 200

    changing_account-=100
    assert changing_account.balance == 100
