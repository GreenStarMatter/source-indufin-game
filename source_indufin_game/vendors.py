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
        self._is_player = self.vendor_name.split(" ") == "Player"
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
                          "cost",
                          "process_time",
                          "capacity"]
        vendor_catalogue = [["None", "None", "None", 0, 0, 0, 0, 0]]
        return pd.DataFrame(vendor_catalogue, columns = vendor_columns)


    def check_records_exist(self, verify_catalogue_record_df):
        """This method takes a single row Pandas dataframe and verifies if
        that row already exists in the catalogue.  Method could take multiple;
        however, to maintain integrity of ledger only one is processed at a
        time."""

        #maybe put temp variable to keep index of row to be changed?
        index_columns = ["vendor_type", "product_type",
                         "form", "potency", "process_time", "capacity"]
        index_df = verify_catalogue_record_df[index_columns].copy()
        exists = pd.merge(self.catalogue.reset_index(drop = False), index_df,
                          how = 'inner', on = index_columns)
        return list(exists["index"])


    def _in_place_add_to_catalogue_stock(self, update_df,
                                         temporary_index_store):
        replace_row = self.catalogue.iloc[temporary_index_store].copy()
        replace_row["stock"] += update_df["stock"].values
        self.catalogue.iloc[temporary_index_store] = replace_row


    def _in_place_subtract_from_catalogue_stock(self, update_df,
                                                temporary_index_store):
        replace_row = self.catalogue.iloc[temporary_index_store].copy()
        replace_row["stock"] -= update_df["stock"].values
        if replace_row["stock"].values >= 0:
            self.catalogue.iloc[temporary_index_store] = replace_row
        else:
            print("Not enough stock to complete sale, off by: "+
                  f"{-replace_row['stock'].values[0]}")


    def update_catalogue(self, method, update_df):
        """Updates catalogue with a predefined method.
        Current Options:
        Purchase: Purchase goes into catalogue to check if record exists.
        If it does, then purchase iterates the stock value
        If it does not, then purchase add a new catalogue row
        Sell: Sell reduces stock in catalogue"""

        update_successful = True
        temporary_index_store = self.check_records_exist(update_df)
        if method == "Purchase":
            if temporary_index_store:
                self._in_place_add_to_catalogue_stock(update_df,
                                                      temporary_index_store)
            else:
                self.catalogue = pd.concat([self.catalogue, update_df],
                                           ignore_index = True)
        elif method == "Sell":
            if temporary_index_store:
                self._in_place_subtract_from_catalogue_stock(
                    update_df,
                    temporary_index_store
                    )
            else:
                update_successful = False
                print(f"Item does not exist in catalogue:{chr(10)}{update_df}")
        return update_successful
    def purchase_from_vendor(self, selling_vendor, update_df):
        """This function allows a the current vendor object to purchase
        from another vendor object.  Currently it will only work where all
        are purchasers.  May implement a sell to vendor in future."""

        transaction_complete = False
        sell_condition = 0
        seller_update_df = update_df.copy()
        seller_update_df["vendor_type"] = "Sell"
        if selling_vendor.sale_is_possible(seller_update_df):
            sell_condition += 1
        else:
            print("Seller stock too low")

        if self.purchase_is_possible(update_df):
            sell_condition += 1
        else:
            print("Not enough buyer money for transaction")

        if sell_condition == 2:
            transaction_complete = True
            self.update_catalogue("Purchase", update_df)
            selling_vendor.update_catalogue("Sell", seller_update_df)
            self.account.purchase_from(selling_vendor.account, update_df)
            print("Item and Financial Transaction Completed")
        else:
            print("Transaction Failed")

        return transaction_complete


    def sale_is_possible(self, update_df):
        """Verifies external vendor has enough supply for transaction"""

        sale_status = False
        temporary_index_store = self.check_records_exist(update_df)
        if temporary_index_store:
            seller_stock = self.catalogue\
                .iloc[temporary_index_store]["stock"].values
            stock_balance = seller_stock - update_df["stock"].values
            if stock_balance >= 0:
                sale_status = True
        return sale_status


    def purchase_is_possible(self, update_df):
        """Verifies this vendor has enough money to complete transaction"""

        return self.account.verify_purchase_possible(update_df)
