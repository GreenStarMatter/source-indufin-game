# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:43:51 2022

@author: Kyle Stanley


This tests the core accounting logic.  This will be the storage of money
and the ability to create simple changes to those balances.
"""


from source_indufin_game import accounts
import pandas as pd

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

def test_multiple_account_exchange():
    """Tests balance changing logic of account class"""

    buying_account = accounts.MoneyAccount()
    selling_account = accounts.MoneyAccount()
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost"]
    catalogue_update = [["Buy", "Testonium", "Bar",
                        3, 2, 30]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    buying_account.set_balance(100)
    selling_account.set_balance(100)
    buying_account.purchase_from(selling_account, update_df)
    assert buying_account.balance == 40
    assert selling_account.balance == 160

    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost"]
    catalogue_update = [["Buy", "Testonium", "Bar",
                        3, 2, 30]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    buying_account.set_balance(50)
    selling_account.set_balance(100)
    buying_account.purchase_from(selling_account, update_df)
    assert buying_account.balance == 50
    assert selling_account.balance == 100
