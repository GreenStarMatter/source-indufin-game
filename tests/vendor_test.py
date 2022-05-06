# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:11:32 2022

@author: Kyle Stanley
"""

from source_indufin_game import vendors
from source_indufin_game import accounts
import pandas as pd


def test_vendor_object_shape():
    """Basic form test of processor"""

    basic_vendor = vendors.Vendor()

    assert basic_vendor.vendor_name == "None Assigned"
    assert basic_vendor.vendor_type == "None" #"Buyer","Seller","None","Both"
    assert basic_vendor.account
    #Shape: {Buy:{machine_name:[augment, augment_potency, stock/cap, cost]}}
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    vendor_catalogue = [["None", "None", "None",
                         0, 0, 0, 0]]
    vendor_df = pd.DataFrame(vendor_catalogue, columns = vendor_columns)
    assert basic_vendor.catalogue.equals(vendor_df)


def test_vendor_altering_shape():
    """Test setting variables"""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    vendor_catalogue = [["Buy", "Testonium", "Bar", 0, 50, 100, -1]]
    vendor_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    vendor_df = pd.DataFrame(vendor_catalogue, columns = vendor_columns)
    basic_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = vendor_df
        )
    assert basic_vendor.vendor_name == "Vendor 1"
    assert basic_vendor.vendor_type == "Buyer"
    assert basic_vendor.catalogue.equals(vendor_df)

def test_vendor_transaction_successful():
    """Test setting variables"""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    buyer_catalogue = [["Buy", "Testonium", "Bar", 0, 50, 100, -1]]
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    buyer_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    buyer_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = buyer_df
        )
    seller_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    seller_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = seller_df
        )
    buyer_vendor.account.set_balance(1000)
    seller_vendor.account.set_balance(1000)
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    catalogue_update = [["Buy", "Testonium", "Bar",
                        0, 2, 100, -1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    buyer_vendor.purchase_from_vendor(seller_vendor, update_df)

    new_buyer_catalogue = [["Buy", "Testonium", "Bar", 0, 52, 100, -1]]
    new_buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    new_buyer_df = pd.DataFrame(new_buyer_catalogue, columns = vendor_columns)
    assert buyer_vendor.catalogue.equals(new_buyer_df)
    new_seller_catalogue = [["Buy", "Testonium", "Bar", 0, 48, 100, -1]]
    new_seller_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    new_seller_df = pd.DataFrame(new_seller_catalogue,
                                 columns = vendor_columns)
    assert seller_vendor.catalogue.equals(new_seller_df)

def test_vendor_transaction_insufficient_funds():
    """Test setting variables"""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    buyer_catalogue = [["Buy", "Testonium", "Bar", 0, 50, 100, -1]]
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    buyer_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    buyer_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = buyer_df
        )
    seller_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    seller_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = seller_df
        )
    buyer_vendor.account.set_balance(150)
    seller_vendor.account.set_balance(1000)
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    catalogue_update = [["Buy", "Testonium", "Bar",
                        0, 2, 100, -1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    buyer_vendor.purchase_from_vendor(seller_vendor, update_df)

    assert buyer_vendor.catalogue.equals(buyer_df)
    assert seller_vendor.catalogue.equals(seller_df)

def test_vendor_transaction_insufficient_stock():
    """Test setting variables"""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    buyer_catalogue = [["Buy", "Testonium", "Bar", 0, 1, 100, -1]]
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 3, 100000, 3])
    buyer_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    buyer_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = buyer_df
        )
    seller_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    seller_vendor = vendors.Vendor(
        vendor_name = "Vendor 1",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = seller_df
        )
    buyer_vendor.account.set_balance(1000)
    seller_vendor.account.set_balance(1000)
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    catalogue_update = [["Buy", "Testonium", "Bar",
                        0, 2, 100, -1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    buyer_vendor.purchase_from_vendor(seller_vendor, update_df)

    assert buyer_vendor.catalogue.equals(buyer_df)
    assert seller_vendor.catalogue.equals(seller_df)
