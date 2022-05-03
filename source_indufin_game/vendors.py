# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:11:29 2022

@author: Kyle Stanley
"""
import pandas as pd
from source_indufin_game import accounts

class Vendor():
    """Documentation goes here"""

    def __init__(self,
                 catalogue = pd.DataFrame(),
                 vendor_name = "None Assigned",
                 vendor_type = "None",
                 account = accounts.MoneyAccount(),
                 ):

        self.vendor_name = vendor_name
        self.vendor_type = vendor_type
        self.account = account
        self.temporary_index_store = -1
        if not catalogue.empty:
            self.catalogue = catalogue
        else:
            self.catalogue = self._EMPTY_CATALOGUE()


    def _EMPTY_CATALOGUE(self):
        """Instances an empty catalogue data structure.  Internal method
        meant to be a placeholder."""
        vendor_columns = ["vendor_type",
                          "product_type",
                          "form",
                          "potency",
                          "stock",
                          "cost"]
        vendor_catalogue = [["None", "None", "None", 0, 0, 0]]
        return pd.DataFrame(vendor_catalogue, columns = vendor_columns)


    def check_records_exist(self, verify_catalogue_record_df):
        """This method takes a single row Pandas dataframe and verifies if
        that row already exists in the catalogue.  Method could take multiple;
        however, to maintain integrity of ledger only one is processed at a
        time."""

        #maybe put temp variable to keep index of row to be changed?
        index_columns = ["vendor_type", "product_type", "form", "potency"]
        index_df = verify_catalogue_record_df[index_columns].copy()
        exists = pd.merge(self.catalogue.reset_index(drop = False), index_df,
                          how = 'inner', on = index_columns)
        self.temporary_index_store = list(exists["index"])
        return not exists.empty

    def _in_place_add_to_catalogue_stock(self, update_df):
        replace_row = self.catalogue.iloc[self.temporary_index_store].copy()
        replace_row["stock"] += update_df["stock"].values
        self.catalogue.iloc[self.temporary_index_store] = replace_row


    def _in_place_subtract_from_catalogue_stock(self, update_df):
        replace_row = self.catalogue.iloc[self.temporary_index_store].copy()
        replace_row["stock"] -= update_df["stock"].values
        if replace_row["stock"].values > 0:
            self.catalogue.iloc[self.temporary_index_store] = replace_row
        else:
            print("Not enough stock to complete sale, off by:"+
                  f"{-replace_row['stock'].values[0]}")


    def update_catalogue(self, method, update_df):
        """Updates catalogue with a predefined method.
        Current Options:
        Purchase: Purchase goes into catalogue to check if record exists.
        If it does, then purchase iterates the stock value
        If it does not, then purchase add a new catalogue row
        Sell: Sell reduces stock in catalogue"""

        if method == "Purchase":
            if self.check_records_exist(update_df):
                self._in_place_add_to_catalogue_stock(update_df)
            else:
                self.catalogue = pd.concat([self.catalogue, update_df])
        elif method == "Sell":
            if self.check_records_exist(update_df):
                self._in_place_subtract_from_catalogue_stock(update_df)
            else:
                print(f"Item does not exist in catalogue:{chr(10)}{update_df}")

    def purchase_from_vendor(self, selling_vendor, update_df):
        """This function allows a the current vendor object to purchase
        from another vendor object.  Currently it will only work where all
        are purchasers.  May implement a sell to vendor in future."""
        sell_condition = 0
        if selling_vendor.sale_is_possible(selling_vendor, update_df):
            sell_condition += 1
        else:
            print("Seller stock too low")

        if self.purchase_is_possible(update_df):
            sell_condition += 1
        else:
            print("Not enough buyer money for transaction")

        if sell_condition == 2:
            self.update_catalogue("Purchase", update_df)
            selling_vendor.update_catalogue("Sell", update_df)
            self.account.purchase_from(selling_vendor.account, update_df)
            print("Item and Financial Transaction Completed")
        else:
            print("Transaction Failed")


    def sale_is_possible(self, selling_vendor, update_df):
        """Verifies external vendor has enough supply for transaction"""

        sale_status = False
        if selling_vendor.check_records_exist(update_df):
            seller_stock = selling_vendor.catalogue\
                .iloc[selling_vendor.temporary_index_store]["stock"].values
            stock_balance = seller_stock - update_df["stock"].values
            if stock_balance >= 0:
                sale_status = True
        return sale_status


    def purchase_is_possible(self, update_df):
        """Verifies this vendor has enough money to complete transaction"""

        return self.account.verify_purchase_possible(update_df)
