# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:38:09 2022

@author: Kyle Stanley
"""

import basic_tutorial
import pandas as pd


############################################################################
###Asset creation tests
def test_buyer_creation():
    """Tests the creation of the buyer assets"""

    new_buyer = basic_tutorial.create_buyer_vendor()
    assert new_buyer


def test_seller_creation():
    """Tests the creation of the seller assets"""

    new_seller = basic_tutorial.create_seller_vendor()
    assert new_seller

def test_grid_creation():
    """Tests the creation of the grid asset"""

    new_grid = basic_tutorial.create_factory_grid()
    assert new_grid


def test_player_creation():
    """Tests the creation of the player asset"""

    new_player = basic_tutorial.create_player(500)
    assert new_player.account.balance == 500

def test_new_machine_generation():
    """Test the generation of machines"""

    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    catalogue_update = [["Sell", "Testulator", "Melt",
                        3, 1, 60, 1, 5]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    new_machine = basic_tutorial.generate_new_machine(update_df)

    assert new_machine.machine_name == "Testulator"
    assert new_machine.augment == "Melt"
    assert new_machine.augment_potency == 3
    assert new_machine.capacity == 5

def test_new_processor_generation():
    """Test the generation of machines"""

    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    catalogue_update = [["Sell", "Testulator", "Melt",
                        3, 1, 60, 1, 5]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    new_machine = basic_tutorial.generate_new_machine(update_df)
    new_processor = basic_tutorial.generate_new_processor(new_machine)
    
    assert new_processor.mechanism == new_machine

def test_new_payload_generation():
    """Test the generation of machines"""

    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    catalogue_update = [["Sell", "Testonium", "Bar",
                        0, 5, 0, -1, -1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    new_payload = basic_tutorial.generate_new_payload(update_df)
    #new_processor = basic_tutorial.generate_new_processor(new_machine)
    
    assert new_payload[1] == 5
    assert new_payload[0].material_name == "Testonium"
    assert new_payload[0].form == "Bar"
    assert new_payload[0].form_potency == 0

    
