# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:38:07 2022

@author: Kyle Stanley
"""

import string
import pandas as pd
import sys

from source_indufin_game import vendors
from source_indufin_game import accounts
from source_indufin_game import machines
from source_indufin_game import materials
from source_indufin_game import grid
from source_indufin_game import processors

############################################################################
###Gameflow helper functions
def win_condition_check(win_threshold, player):
    win_condition = win_threshold <= player.account.balance
    if win_condition:
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
    return win_condition
def evaluate_quit(player_input):
    player_quit = False
    if player_input == "quit":
        player_input = input("Are you sure? (y) to quit")
        if player_input == "y":
            player_quit = True
    return player_quit

def enumerate_list_for_clean_print(player_options):
    """Yes it could be more readible, but everybody gets one show-off.  Offers
    great condensed print menu for up to 10 items."""

    return "\n".join((map((lambda x,y: x+ ": " +y),
                                    player_options,
                                    string.digits[:len(player_options)])))
def decrement_all_processors(processors_available):
    """Progresses all processors by a turn"""
    if processors_available:
        for processor in processors_available.values():
            processor.decrement_processor_tracker()

def index_all_grid_machines_for_player_readability(factory):
    """Indexes all machines for easier programatic access"""
    easy_index_items = {}
    for obj_ind, board_object in enumerate(factory.objects_on_grid.keys()):
        easy_index_items[factory.objects_on_grid[board_object]] = [
            board_object.__repr__(),
            obj_ind,
            board_object]

    return easy_index_items

def check_stock_amount_valid(update_df, stock_check_value):
    """Verify that catalogue has enough stock to perform transaction"""

    return update_df["stock"].values[0] >= stock_check_value

def print_vendor_for_ux(vendor):
    """Pretty print of vendor data so user can browse catalogue"""

    print()
    print(f"***{vendor.vendor_name}***")
    print()
    print(vendor.catalogue)
    return None

def get_all_available_machines_for_placement(grid,
                                             processors_available,
                                             all_machines_on_grid):
    """Pretty print of all machines and the index to select them.  Also shows
    if the machine is ready to accept a new payload"""

    all_machines_on_grid = list(grid.objects_on_grid.keys())
    for mach_ind, machine in enumerate(all_machines_on_grid):
        processor = processors_available[machine]
        machine_available = (processor.output_payload is None)\
            and (processor._processing_flag == 0)
        availability = "Processing"
        if machine_available:
            availability = "Available"
        print("*****************************************")
        print(f"{mach_ind} : {machine.machine_name} : {availability}")
        print(machine.__str__())
        print("*****************************************")
        print()

def get_all_available_materials_for_placement(start_ind_of_materials,
                                              all_ready_processors):
    """Pretty print of all materials which are ready for harvesting."""
    
    for processor_ind, processor in enumerate(all_ready_processors):
        output_payload = processor.output_payload
        print("*****************************************")
        print(f"{start_ind_of_materials + processor_ind} :"+
              f" {output_payload[0].material_name} {output_payload[0].form}"+
              f" {output_payload[0].form_potency}: {output_payload[1]}")
        print("*****************************************")
        print()


def get_associated_player_stock_from_buyer_cat(player, catalogue_row):
    """Matches the player stock to the selected buying option to verify
    that player can attempt sale"""

    item_exists = False
    temp = catalogue_row.copy()
    temp["vendor_type"] = "Sell"
    existence_index = player.check_records_exist(temp)
    if existence_index:
        item_exists = True
        catalogue_row["stock"] =\
            player.catalogue.loc[existence_index]["stock"].values[0]
    else:
        print("Item not in player catalogue")

    return item_exists


def convert_coordinates_to_tuple(coordinate_string):
    """Converts input string of the form xy into a coordinate tuple"""

    return (int(coordinate_string[0]), int(coordinate_string[1]))

def get_all_materials_that_are_ready_for_removal(all_ready_processors,
                                                 start_ind_of_materials):
    
    for cur_ind, processor in enumerate(all_ready_processors):
        actual_ind = start_ind_of_materials + cur_ind
        print(actual_ind + " : " + processor.output_payload)
############################################################################

############################################################################
###Asset creation functions
#Buyer
def create_buyer_vendor():
    """Creates buyer vendor."""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    buyer_catalogue = [["Buy", "Testonium", "Melted", 3, 0, 8, -1, -1]]
    buyer_catalogue.append(["Buy", "Experimentallite",
                            "Melted", 3, 0, 6, -1, -1])
    buyer_catalogue.append(["Buy", "Pilotine", "Melted", 3, 0, 4, -1, -1])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 30, 5])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 150, 25])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 600, 100])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 24, 12])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 100, 50])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 400, 200])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 34, 50])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 67, 100])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 100, 150])
    buyer_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    buyer_vendor = vendors.Vendor(
        vendor_name = "Bobby the Buyer",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = buyer_df
            )
    buyer_vendor.account.set_balance(1000000000000)
    return buyer_vendor

#Seller
def create_seller_vendor():
    """"Create seller vendor"""
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    seller_catalogue = [["Sell", "Testonium", "Bar", 0, 100000000, 5, -1, -1]]
    seller_catalogue.append(["Sell", "Experimentallite", "Bar",
                             0, 100000000, 4, -1, -1])
    seller_catalogue.append(["Sell", "Pilotine", "Bar",
                             0, 100000000, 3, -1, -1])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 5, 60, 1, 5])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 25, 300, 1, 25])
    seller_catalogue.append(["Sell", "Testulator", "Melt",
                             3, 50, 1200, 1, 100])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 5, 48, 2, 12])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 25, 200, 2, 50])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt",
                             3, 50, 800, 2, 200])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 5, 67, 3, 50])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 25, 134, 3, 100])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 50, 200, 3, 150])
    seller_df = pd.DataFrame(seller_catalogue, columns = vendor_columns)
    seller_vendor = vendors.Vendor(
        vendor_name = "Sal the Seller",
        vendor_type = "Seller",
        account = accounts.MoneyAccount(),
        catalogue = seller_df
            )
    seller_vendor.account.set_balance(0)
    return seller_vendor

#Grid
def create_factory_grid():
    """"Create grid"""

    return grid.FactoryGrid((6,6))

#Player
def create_player(starting_balance = 1000):
    """Create player, currently player is a vendor"""
    player = vendors.Vendor(
        vendor_name = "Player 1",
        vendor_type = "Both",
        account = accounts.MoneyAccount(),
            )
    player.account.set_balance(starting_balance)#300)
    return player
#Machine
def generate_new_machine(update_df):
    """Generates a machine when a reference is passed.  This can be thought of
    as the reference holding a spot in a catalogue.  When the item is ordered
    this function creates the item that the catalogue was referring to."""

    machine_identity_info = list(update_df[[
                             'product_type',
                             'form',
                             'potency',
                             'process_time',
                             'capacity'
                             ]].values[0])
    shape = {1:[[1]],
             2:[[1,1], [1,1]],
             3:[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]}
    processible_inputs = {"Testulator" : ["Testonium"],
                          "Exbopulator" : ["Experimentallite"],
                          "Pilomatic" : ["Pilotine"]}

    new_machine = machines.MachineUnit(
    cost = update_df["cost"].iloc[0],
    shape = shape[machine_identity_info[3]],
    owner = "Player 1",
    machine_name = update_df["product_type"].iloc[0],
    processable_inputs = processible_inputs[update_df["product_type"].iloc[0]],
    augment = update_df["form"].iloc[0],
    augment_potency = update_df["potency"].iloc[0],
    capacity = update_df["capacity"].iloc[0],
    turns_to_process = update_df["process_time"].iloc[0])
    
    return new_machine

#Processor
def generate_new_processor(new_machine):
    """Generates a new processor.  This is gives a machine transaction
    capabilities for materials."""

    new_processor = processors.ProcessorUnit(mechanism = new_machine)
    return new_processor

#Payload
def generate_new_payload(update_df):
    """Generates a payload from a reference."""
    print("++++++++++++++++++++++++++++++++++++++")
    print(update_df)
    print("++++++++++++++++++++++++++++++++++++++")

    material_identity_info = list(update_df[[
                             'product_type',
                             'form',
                             'potency',
                             'stock'
                             ]].values[0])

    new_material = materials.MaterialUnit(
        cost = 0,
        owner = "Player 1",
        material_name = material_identity_info[0],
        form = material_identity_info[1],
        form_potency = material_identity_info[2])    

    return [new_material, material_identity_info[3]]
############################################################################

############################################################################
###Transactions
def move_item_from_seller_to_player_catalogue(player, seller, update_df):
    """Transacts a purchase to the player from a seller"""

    player.purchase_from_vendor(seller, update_df)
    player.catalogue["vendor_type"] = "Sell"


def move_item_from_player_to_buyer_catalogue(player, buyer, update_df):
    """Transacts a sale to a buyer from the player"""

    buyer.purchase_from_vendor(player, update_df)
    player.catalogue["vendor_type"] = "Sell"

def move_machine_from_player_catalogue_to_grid(player,
                                               factory,
                                               processors_available,
                                               update_df,
                                               coordinates):
    """Transacts a machine out of the players catalogue and places it on
    the grid.  Creates a processor corresponding to the machine as well."""
    #TODO: Verify player has suffient Stock... or remove 0 stock items from inventory
    successful_transaction = False
    object_to_place = generate_new_machine(update_df)
    transaction_gate_1 = player.check_records_exist(update_df)
    transaction_gate_2 = factory.verify_valid_placement(object_to_place,
                                                        coordinates)
    
    if not transaction_gate_1:
        print("Record doesn't exist for player")
    elif not transaction_gate_2:
        print("Invalid placement of machine")
    else:
        player.update_catalogue("Sell", update_df)
        new_processor = generate_new_processor(object_to_place)
        processors_available[object_to_place] = new_processor
        factory.place_on_grid(object_to_place, coordinates)
        successful_transaction = True
    return successful_transaction


def move_material_from_player_catalogue_to_machine(
        player, factory, processors_available,
        update_df, player_input_coordinates_of_machine):
    """Transacts a material out of the player catalogue and into a machine
    already placed on the grid."""

    transaction_successful = True
    input_payload = generate_new_payload(update_df)
    transaction_gate_1 = player.check_records_exist(update_df)
    easy_index_items = \
        index_all_grid_machines_for_player_readability(factory)
    machine_to_place_into =\
        easy_index_items[player_input_coordinates_of_machine][2]
    processor_to_place_into = \
        processors_available[machine_to_place_into]
    transaction_gate_2 = \
        processor_to_place_into\
            .verify_payload_machine_viability_tests(input_payload)

    if not transaction_gate_1:
        transaction_successful = False
        print("Record doesn't exist for player")
    elif not transaction_gate_2:
        transaction_successful = False
        print("Invalid placement of material")
    else:
        player.update_catalogue("Sell", update_df)
        processor_to_place_into.set_payload(input_payload)

    return transaction_successful


def move_material_in_processor_into_player_catalogue(player, processor):
    """Transacts a material which has been processed out of a processor
    and into the player's catalogue."""

    valid_transaction = False
    if not processor.output_payload_ready():
        print("Output paylod not read yet")
    else:
        valid_transaction = True
        output_payload = processor.collect_output_payload()
        update_columns = ["vendor_type", "product_type", "form",
                          "potency", "stock", "cost", "process_time"]
        catalogue_update = [["Sell", output_payload[0].material_name,
                             output_payload[0].form,
                            output_payload[0].form_potency, output_payload[1],
                            0, -1]]
        update_df = pd.DataFrame(catalogue_update, columns = update_columns)
        player.update_catalogue("Purchase", update_df)

    return valid_transaction


def move_machine_from_grid_into_player_catalogue(
        player, factory, processors_available,
        player_input_coordinates_to_transform, update_df):
    """Transacts a machine from the grid back into a player's catalogue"""

    #TODO: Verify if item is in processor
    #If so auto-collect if ready, ask player "Are you sure" if not
    transaction_valid = False
    easy_index_items = \
        index_all_grid_machines_for_player_readability(factory)
    
    transaction_gate_1 =\
        player_input_coordinates_to_transform in easy_index_items.keys()
    
    if transaction_gate_1:
        transaction_valid = True
        object_to_remove = easy_index_items[
        player_input_coordinates_to_transform
        ][2]
        #If machine on board
        player.update_catalogue("Purchase", update_df)
        #remove from grid
        factory.remove_from_grid(object_to_remove)
        del processors_available[object_to_remove]
        
    else:
        print("No object at those coordinates")

    return transaction_valid
############################################################################

############################################################################
###Update Data Frame Helper Functions
def create_purchase_update_df(catalogue_row, purchase_amount):
    """Create catalogue update by changing the stock to the purchase amount"""

    update_df = catalogue_row.copy()
    update_df["stock"] = int(purchase_amount)

    return update_df


def create_sale_update_df(catalogue_row, sale_amount):
    """Create catalogue update by changing the stock to the sale amount"""

    update_df = catalogue_row.copy()
    update_df["stock"] = int(sale_amount)

    return update_df

def create_material_placement_update_df(catalogue_row, place_amount):
    """Create catalogue update for placing a material"""

    update_df = catalogue_row.copy()
    update_df["stock"] = int(place_amount)
    update_df["cost"] = 0

    return update_df

def create_machine_removed_from_grid_update_df(machine):
    """Create catalogue update for removing a machine from the grid"""

    update_columns = ["vendor_type", "product_type", "form",
                  "potency", "stock", "cost", "process_time", "capacity"]
    catalogue_update = [["Sell", machine.machine_name, machine.augment,
                        machine.augment_potency, 1,
                        0, machine.turns_to_process, machine.capacity]]
    update_df = pd.DataFrame(catalogue_update, columns = update_columns)

    return update_df  
############################################################################

############################################################################
###Player Decision Tree
def player_decision_choose_quantity_to_purchase(player, seller, catalogue_row):
    """Takes player input to get the quantity of the item being purchased"""
    
    player_input_catalogue_check_valid = False
    while not player_input_catalogue_check_valid:
        amount_prompt = "Select item amount or (m) for main menu:"
        player_input = input(amount_prompt)
        if player_input.isdigit():
            player_input_catalogue_check_valid =\
                check_stock_amount_valid(catalogue_row, int(player_input))
        invalid_input = (not player_input.isdigit()) and (player_input != "m")
        if invalid_input:
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_catalogue_check_valid = True
        elif player_input_catalogue_check_valid:
            update_df = create_purchase_update_df(
                catalogue_row, int(player_input))
            move_item_from_seller_to_player_catalogue(
                player, seller, update_df)

        else:
            print("Input invalid, please try again.")
    
    return None


def player_decision_choose_quantity_to_sell(player, buyer, catalogue_row):
    """Takes player input to get the quantity of the item being sold"""

    player_input_catalogue_check_valid = False
    while not player_input_catalogue_check_valid:
        amount_prompt = "Select item amount or (m) for main menu:"
        player_input = input(amount_prompt)
        if player_input.isdigit():
            player_input_catalogue_check_valid =\
                check_stock_amount_valid(catalogue_row, int(player_input))
        if (not player_input.isdigit()) and (player_input != "m"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_catalogue_check_valid = True
        elif player_input_catalogue_check_valid:
            update_df = create_sale_update_df(
                catalogue_row, int(player_input))
            move_item_from_player_to_buyer_catalogue(
                player, buyer, update_df)
        else:
            print("Input invalid, please try again.")
    
    return None

def player_decision_seller_catalogue_branch(player, seller):
    """Takes player input to decide which item in seller catalogue will be 
    purchased"""
    
    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu:"
        player_input = input(item_prompt)
        #player_input_catalogue_check_valid = False
        
        if (not player_input.isdigit()) and (player_input != "m"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_check_valid_item = True
        elif int(player_input) in seller.catalogue.index:
            player_input = int(player_input)
            catalogue_row = seller.catalogue.loc[[player_input]]
            player_decision_choose_quantity_to_purchase(player, seller,
                                                        catalogue_row)
            player_input_check_valid_item = True
        else:
            print("Input invalid, please try again.")
    return None

def player_decision_buyer_catalogue_branch(player, buyer):
    """Takes player input to decide which item in buyer catalogue will be 
    sold"""

    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu:"
        player_input = input(item_prompt)
        #player_input_catalogue_check_valid = False
        
        if (not player_input.isdigit()) and (player_input != "m"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_check_valid_item = True
        elif int(player_input) in buyer.catalogue.index:

            catalogue_row = buyer.catalogue.loc[[int(player_input)]]
            if get_associated_player_stock_from_buyer_cat(
                    player, catalogue_row):
                player_decision_choose_quantity_to_sell(player, buyer,
                                                            catalogue_row)
                player_input_check_valid_item = True
                
        else:
            print("Input invalid, please try again.")
    return None

def player_decision_buy_or_sell_branch(player, buyer, seller):
    """Takes player input whether the player wants to interact with a buyer or
    with a seller"""

    valid_buy_sell = False
    while not valid_buy_sell:
        buy_sell_prompt = "Enter 1 to buy, 2 to sell, " +\
            "(m) to return to main menu: "
        player_input = input(buy_sell_prompt)
        
        if player_input == "1":
            valid_buy_sell = True
            print_vendor_for_ux(seller)
            player_decision_seller_catalogue_branch(player, seller)
        elif player_input == "2":
            valid_buy_sell = True
            print(player.catalogue)
            print_vendor_for_ux(buyer)
            #Change to buyer in function name, make buy function
            player_decision_buyer_catalogue_branch(player, buyer)
        elif player_input == "m":
            valid_buy_sell = True
        else:
            print("Input invalid, please try again.")


def player_decision_select_machine_for_placement(player,
                                                 grid,
                                                 processors_available,
                                                 catalogue_row):
    """Player input decision to choose a machine to place from catalogue onto
    grid"""

    player_input_to_choose_machine_valid = False
    all_machines_on_grid = list(grid.objects_on_grid.keys())
    while not player_input_to_choose_machine_valid:
        get_all_available_machines_for_placement(grid,
                                                 processors_available,
                                                 all_machines_on_grid)
        machine_choice_prompt = "Choose the index of a machine to place"+\
            " material in or (m) for main menu: "
        material_amount_prompt = "Choose the amount to place in machine: "
        player_input_machine = input(machine_choice_prompt)
        if material_amount_prompt == "m":
            player_input_amount = 0
        else:
            player_input_amount = input(material_amount_prompt)

        if (not player_input_machine.isdigit())\
            and (player_input_machine != "m")\
                and (not player_input_amount.isdigit()):
            print("Input invalid, please try again.")
        elif player_input_machine == "m":
            player_input_to_choose_machine_valid = True
        elif int(player_input_machine)>len(all_machines_on_grid) or\
            int(player_input_machine)<0:
            print("Input invalid, please try again.")
        else:
            player_input_to_choose_machine_valid = True
            machine = all_machines_on_grid[int(player_input_machine)]
            player_input_coordinates_of_machine = grid.objects_on_grid[machine]
            update_df =\
                create_material_placement_update_df(catalogue_row,
                                                    int(player_input_amount))
            print(update_df)
            player_input_to_choose_machine_valid =\
                move_material_from_player_catalogue_to_machine(
                    player, grid, processors_available,
                    update_df, player_input_coordinates_of_machine)

def player_decision_item_type_of_choice_branch(player,
                                               grid,
                                               processors_available,
                                               catalogue_row):
    """Passes catalogue selection to branch to materials or machine options"""
    
    if catalogue_row["process_time"].values[0] == -1:
        player_decision_select_machine_for_placement(
            player, grid, processors_available, catalogue_row)
    else:
        player_input_machine_placement_process(
            player, grid, processors_available, catalogue_row)

    return None

def player_decision_player_catalogue_branch(player,
                                            processors_available,
                                            grid):
    """Player input decision to choose an item from own catalogue to place on
    grid"""

    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu:"
        player_input = input(item_prompt)
        if (not player_input.isdigit()) and (player_input != "m"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_check_valid_item = True
        elif int(player_input) in player.catalogue.index:
            catalogue_row = player.catalogue.loc[[int(player_input)]]
            player_decision_item_type_of_choice_branch(player,
                                                       grid,
                                                       processors_available,
                                                       catalogue_row)
            player_input_check_valid_item = True
        else:
            print("Input invalid, please try again.")
    return None


def player_decision_remove_from_grid_branch(player,
                                            processors_available,
                                            grid):
    """Placer decision to remove an item from the grid.  Lists all viable
    materials and machines which could be removed"""
    
    player_input_check_valid_item = False
    all_machines_on_grid = list(grid.objects_on_grid.keys())
    start_ind_of_materials = len(all_machines_on_grid)
    all_ready_processors = [processors_available[machine]\
                           for machine in all_machines_on_grid if\
                               processors_available[machine].\
                                   output_payload_ready_flag == 1]
    while not player_input_check_valid_item:
        get_all_available_machines_for_placement(grid,
                                             processors_available,
                                             all_machines_on_grid)
        get_all_available_materials_for_placement(start_ind_of_materials,
                                                  all_ready_processors)

        player_input = input("Select object for removal")
        if player_input.isdigit():
            list_ind = int(player_input)


        if (not player_input.isdigit()) and (player_input != "m"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_check_valid_item = True
        elif list_ind < len(all_machines_on_grid):
            #get coordinates from list choice
            machine = all_machines_on_grid[list_ind]
            machine_coords = grid.objects_on_grid[machine]
            update_df =\
                create_machine_removed_from_grid_update_df(machine)
            player_input_check_valid_item =\
                move_machine_from_grid_into_player_catalogue(
                    player, grid, processors_available,
                    machine_coords, update_df)
        elif list_ind >= len(all_machines_on_grid) and\
            (int(player_input) < start_ind_of_materials\
                + len(all_ready_processors)):
            list_ind -= start_ind_of_materials
            processor = all_ready_processors[list_ind]
            
            player_input_check_valid_item =\
                move_material_in_processor_into_player_catalogue(
                    player, processor)
        else:
            print("Input invalid, please try again.")

def player_decision_grid_interaction_branch(player,
                                            grid,
                                            processors_available):
    """Player input to decide to place an item on the grid or to remove an
    item from it"""

    player_input_grid_selection_valid = False
    while not player_input_grid_selection_valid:
        player_input_grid_options = "Select 1 to transfer catalogue " +\
            "item to grid\nSelect 2 to transfer grid item to catalogue\n"+\
                "Select (m) to go to main menu"
        player_input = input(player_input_grid_options)
        if player_input == "1":
            
            print_vendor_for_ux(player)
            print(grid.__str__())
            player_decision_player_catalogue_branch(player,
                                                    processors_available,
                                                    grid)
            player_input_grid_selection_valid = True
        elif player_input == "2":
            player_input_grid_selection_valid = True
            player_decision_remove_from_grid_branch(player,
                                            processors_available,
                                            grid)
        elif player_input == "m":
            player_input_grid_selection_valid = True
        else:
            print("Input invalid, please try again.")


#Slightly different, doesn't branch
def player_input_machine_placement_process(player,
                                           grid,
                                           processors_available,
                                           catalogue_row):
    """Takes player input to determine where a machine should be placed on 
    the grid"""
    transaction_completed = False
    while not transaction_completed:
        print(grid.__str__())
        player_input_grid_placement_string = "Select coordinates for "+\
            "placement (xy)\nSelect (m) to return to main menu\n"
        player_input = input(player_input_grid_placement_string)
        if len(player_input) != 2:
            print("Input invalid, please try again.")
        elif player_input == "m":
            transaction_completed = True
        elif player_input[0].isdigit() and player_input[1].isdigit():
            input_coordinates =\
                convert_coordinates_to_tuple(player_input)
            update_df = catalogue_row.copy()
            update_df["stock"] = 1
            transaction_completed = move_machine_from_player_catalogue_to_grid(
                player, grid, processors_available,
                update_df, input_coordinates)   
        else:
            print("Input invalid, please try again.")
    
############################################################################



def basic_tutorial():
    """Play flow logic for basic game.  Win condition is a simple threshold."""
    win_threshold = 2500
    turn_counter = 0
    buyer = create_buyer_vendor()
    seller = create_seller_vendor()
    player = create_player(300)
    factory = create_factory_grid()
    processors_available = {}
    win_condition_met = False
    player_quit = False
    top_level_player_options = ["Buy/Sell",
                                "Place/Move Item",
                                "List Items",
                                "Help",
                                "End Turn"]
    quit_string = "\n(quit) to quit game"
    while not (win_condition_met or player_quit):
        print(factory.__str__())
        print(f"Current Balance: {player.account.balance}")
        print(player.catalogue)
        command_string = \
            enumerate_list_for_clean_print(top_level_player_options)
        print(command_string + quit_string)
        player_input = input("Enter a commmand: ")
        print()
        print()
        print()
        player_quit = evaluate_quit(player_input)
        if player_input == "0":
            player_decision_buy_or_sell_branch(player, buyer, seller)
        elif player_input == "1":
            player_decision_grid_interaction_branch(player,
                                            factory, processors_available)
        elif player_input == "2":
            print(top_level_player_options[int(player_input)] + " Not Ready")
        elif player_input == "3":
            print(top_level_player_options[int(player_input)] + " Not Ready")
        elif player_input == "4":
            #Need to decrement all processor items here
            turn_counter += 1
            decrement_all_processors(processors_available)
        elif player_input == "quit":
            pass
        else:
            print("Input not recognized")
            
        print()
        print()
        print("*********************************************************")
        #Evaluate player 
        win_condition_met = win_condition_check(win_threshold, player)
    
    print("***********************************GAME END"+
          "***********************************")
     
def main():
    """Runs the basic tutorial game.
    Also sets console pandas print options for better experience."""
    pd.set_option('display.width', 1000)
    pd.set_option('max_columns', None)
    basic_tutorial()


if __name__ == "__main__":
    main()
