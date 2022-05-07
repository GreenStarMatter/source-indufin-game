# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:38:09 2022

@author: Kyle Stanley
"""

from source_indufin_game import basic_tutorial
import pandas as pd
buyer = basic_tutorial.create_buyer_vendor()
seller = basic_tutorial.create_seller_vendor()
player = basic_tutorial.create_player()
factory = basic_tutorial.create_factory_grid()


#T1: Money and machines, purchase from seller to player
###FINISHED, Put in logic
###################################################################
player.account.set_balance(1000000000)
update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time"]
catalogue_update = [["Buy", "Testonium", "Bar",
                    0, 30, 100, -1]]
update_df = pd.DataFrame(catalogue_update, columns = update_columns)
#player purchase machine
transaction = player.purchase_from_vendor(seller, update_df)
player.catalogue["vendor_type"] = "Sell"

update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time"]
catalogue_update = [["Buy", "Testulator", "Melt",
                    3, 1, 0, 1]]
update_df = pd.DataFrame(catalogue_update, columns = update_columns)
transaction = player.purchase_from_vendor(seller, update_df)
player.catalogue["vendor_type"] = "Sell"
###################################################################


#T2:  Machine in player catalogue, place on board
#TODO: Verify player has suffient Stock... or remove 0 stock items from inventory
###################################################################
player.account.set_balance(1000000000)
update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time"]
catalogue_update = [["Sell", "Testulator", "Melt",
                    3, 1, 0, 1]]
update_df = pd.DataFrame(catalogue_update, columns = update_columns)
coordinates = (0,0)
object_to_place = basic_tutorial.generate_new_machine(update_df)
transaction_gate_1 = player.check_records_exist(update_df)
transaction_gate_2 = factory.verify_valid_placement(object_to_place,
                                                    coordinates)
processors_available = {}
if not transaction_gate_1:
    print("Record doesn't exist for player")
elif not transaction_gate_2:
    print("Invalid placement of machine")
else:
    player.update_catalogue("Sell", update_df)
    new_processor = basic_tutorial.generate_new_processor(object_to_place)
    processors_available[object_to_place] = new_processor
    factory.place_on_grid(object_to_place, coordinates)
    
###################################################################

#T3: Material in player catalogue, place in processor
player.account.set_balance(1000000000)
update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time"]
catalogue_update = [["Sell", "Testonium", "Bar",
                    0, 30, 0, -1]]
update_df = pd.DataFrame(catalogue_update, columns = update_columns)
input_payload = basic_tutorial.generate_new_payload(update_df)
transaction_gate_1 = player.check_records_exist(update_df)

player_input_coordinates_of_machine = (0,0)
easy_index_items = \
    basic_tutorial.index_all_grid_machines_for_player_readability(factory)
machine_to_place_into =\
    easy_index_items[player_input_coordinates_of_machine][2]
processor_to_place_into = \
    processors_available[machine_to_place_into]
transaction_gate_2 = \
    processor_to_place_into\
        .verify_payload_machine_viability_tests(input_payload)

if not transaction_gate_1:
    print("Record doesn't exist for player")
elif not transaction_gate_2:
    print("Invalid placement of material")
else:
    player.update_catalogue("Sell", update_df)
    processor_to_place_into.set_payload(input_payload)

#TODO: Do T4
#T4: Material in processor, move to player catalogue
#Select coordinates of machine
#get machine from grid
#get processor from processor dict
#collect output payload if avaialbe
#update player inventory
processor_to_place_into.decrement_processor_tracker()
player_input_coordinates_to_collect_payload = (0,0)
easy_index_items = \
    basic_tutorial.index_all_grid_machines_for_player_readability(factory)
machine_to_place_into =\
    easy_index_items[player_input_coordinates_to_collect_payload][2]
processor_to_place_into = \
    processors_available[machine_to_place_into]
#if payload available
#if 
if not processor_to_place_into.output_payload_ready():
    print("Output paylod not read yet")
else:
    output_payload = processor_to_place_into.collect_output_payload()
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    catalogue_update = [["Sell", output_payload[0].material_name,
                         output_payload[0].form,
                        output_payload[0].form_potency, output_payload[1],
                        0, -1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    player.update_catalogue("Purchase", update_df)
    #create corresponding update_df
    
#collect
#update player catalogue


#T5: Machine in grid, move to player catalogue
###FINSIHED
easy_index_items = \
    basic_tutorial.index_all_grid_machines_for_player_readability(factory)

player_input_coordinates_to_transform = (0,0)
transaction_gate_1 =\
    player_input_coordinates_to_transform in easy_index_items.keys()

if transaction_gate_1:
    object_to_remove = easy_index_items[
    player_input_coordinates_to_transform
    ][2]
    update_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    catalogue_update = [["Sell", "Testulator", "Melt",
                        3, 1, 0, 1]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)
    #If machine on board
    player.update_catalogue("Purchase", update_df)
    #remove from grid
    factory.remove_from_grid(object_to_remove)
    del processors_available[object_to_place]
    
else:
    print("No object at those coordinates")


###################################################################
update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time"]
catalogue_update = [["Buy", "Testonium", "Bar",
                    0, 2, 100, -1]]
update_df = pd.DataFrame(catalogue_update, columns = update_columns)
#T6: Material in player catalogue, sell from player to buyer
###FINISHED
transaction = buyer.purchase_from_vendor(player, update_df)
#T7: Machine is in player catalogue, sell from player to buyer
###FINISHED
transaction = buyer.purchase_from_vendor(player, update_df)
###################################################################