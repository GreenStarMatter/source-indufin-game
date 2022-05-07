# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:38:07 2022

@author: Kyle Stanley
"""

import string
import pandas as pd
from source_indufin_game import vendors
from source_indufin_game import accounts
from source_indufin_game import machines
from source_indufin_game import materials
from source_indufin_game import grid
from source_indufin_game import processors


def set_win_condition():
    pass
def set_processing_bays():
    pass
def set_player():
    pass
def win_condition_check(win_threshold, current_progress):
    pass
def evaluate_quit(player_input):
    player_quit = False
    if player_input == "4":
        player_input = input("Are you sure? Y to quit")
        if player_input == "4":
            player_quit = True
    return player_quit

def enumerate_list_for_clean_print(player_options):
    """Yes it could be more readible, but everybody gets one show-off."""

    return "\n".join((map((lambda x,y: x+ ": " +y),
                                    player_options,
                                    string.digits[:len(player_options)])))





def basic_tutorial():
    win_threshold = 10000
    player_capital = 1000
    win_condition_met = False
    player_quit = False
    buyers = create_buyer_vendor()
    seller = create_seller_vendor()
    factory = create_factory_grid()
    set_processing_bays()
    top_level_player_options = ["Buy/Sell",
                                "Place/Move Item",
                                "List Items",
                                "Help",
                                "End Turn"]
    while not (win_condition_met or player_quit):
        command_string = \
            enumerate_list_for_clean_print(top_level_player_options)
        print(command_string)
        #TODO: Print board, current stats, and objective
        player_input = input("Enter a commmand: ")
        player_quit = evaluate_quit(player_input)
        if player_input == "1":
            #Print all vendors and catalogues (inluding player's)
            #give another player input to select specific vendor (also show player's)
            #After vendor choice give option to choose catalogue option 
            #Choose amount and process
            pass
        elif player_input == "2":
            #print items and locations (grid or loading bay)
            #allow user to select item by number
            #allow user to place item or throw it away
            pass
        elif player_input == "3":
            #print list of all objects in game
            pass
        elif player_input == "4":
            #print long form options
            pass
        else:
            print("Input not recognized")
            
        
        #Evaluate player 
        win_condition_met = win_condition_check(win_threshold, player_capital)

#Buyer ad Seller have matching Inventories
######################################################

######################################################

######################################################
###Buyer

#1 Buyer
#9 Total machines: 3 types with different specs (size and process time)
#3 input materials
#infinite supply
#basic vendor instance
#TODO: this should be overwritten by getting specific machines and taking
#the actual attributes out to fill out the vendors!!!
def create_buyer_vendor():
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    buyer_catalogue = [["Buy", "Testonium", "Melted", 0, 1000000, 100, -1]]
    buyer_catalogue.append(["Buy", "Experimentallite",
                            "Melted", 0, 1000000, 100, -1])
    buyer_catalogue.append(["Buy", "Pilotine", "Melted", 0, 1000000, 100, -1])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 100, 100000, 5])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 100, 100000, 3])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 100, 100000, 1])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 100, 100000, 5])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 100, 100000, 3])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 100, 100000, 1])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 100, 100000, 5])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 100, 100000, 3])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 100, 100000, 1])
    buyer_df = pd.DataFrame(buyer_catalogue, columns = vendor_columns)
    buyer_vendor = vendors.Vendor(
        vendor_name = "Bobby the Buyer",
        vendor_type = "Buyer",
        account = accounts.MoneyAccount(),
        catalogue = buyer_df
            )
    buyer_vendor.account.set_balance(1000000000000)
    return buyer_vendor
######################################################

######################################################
###Seller

#1 Seller
#3 input materials
#infinite purchasing money
def create_seller_vendor():
    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time"]
    seller_catalogue = [["Sell", "Testonium", "Bar", 0, 1000000, 100, -1]]
    seller_catalogue.append(["Sell", "Experimentallite", "Bar",
                             0, 1000000, 100, -1])
    seller_catalogue.append(["Sell", "Pilotine", "Bar", 0, 1000000, 100, -1])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 100, 100000, 5])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 100, 100000, 3])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 100, 100000, 1])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 100, 100000, 5])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 100, 100000, 3])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 100, 100000, 1])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 100, 100000, 5])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 100, 100000, 3])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 100, 100000, 1])
    seller_df = pd.DataFrame(seller_catalogue, columns = vendor_columns)
    seller_vendor = vendors.Vendor(
        vendor_name = "Sal the Seller",
        vendor_type = "Seller",
        account = accounts.MoneyAccount(),
        catalogue = seller_df
            )
    seller_vendor.account.set_balance(1000000000000)
    return seller_vendor
######################################################

######################################################
###Grid
#1 Grid, just pick a size and draw.  Thinking 10 by 10
def create_factory_grid():
    return grid.FactoryGrid((10,10))

def index_all_grid_machines_for_player_readability(factory):
    easy_index_items = {}
    for obj_ind, board_object in enumerate(factory.objects_on_grid.keys()):
        easy_index_items[factory.objects_on_grid[board_object]] = [
            board_object.__repr__(),
            obj_ind,
            board_object]
    return easy_index_items
######################################################

######################################################
###Loading Bay
#1 Incoming loading bay.
#Items that are bought from Seller will appear here
#Player will be able to place these items on factory grid
#Bay will be wiped after every turn
loading_bay = []
def place_in_loading_bay(loading_bay, new_item):
    loading_bay.append(new_item)
    return loading_bay
def remove_from_loading_bay(item_index, grid_location):
    #create machine from 
    pass
def print_loading_bay(loading_bay):
    loading_bay_options = enumerate_list_for_clean_print(loading_bay)
    print(loading_bay_options)
    return None
######################################################

######################################################
###Transactions
#Representing these as functions, but will break them out in actual logic above
#Will be easier to handle them until placement
#Need to define transactions
#Seller -> Loading Bay + Player
def transaction_from_seller_to_player(player, seller, update_df, loading_bay):
    player.purchase_from_vendor(seller, update_df)
    place_in_loading_bay(loading_bay, update_df)
#Loading Bay -> Grid
def transaction_from_loading_bay_to_grid():

    #If machine
    #   #Add Machine matching catalgoue to grid
    #   #Add Processor with machine
    #elif material
    #   #Indicate processor
    #   #Verify Process
    #   #Verify Material Amount
    #   #if Successful, Remove material amount from player catalogue
    #   #if Successful, Remove material from loading bay
    #if successful, Remove from loading bay
    pass
#Loading Bay -> Trash
def transaction_from_loading_bay_to_throw_away():
    return []
def transaction_from_material_to_processor():
    pass
#Grid + Player -> Buyer
def transaction_from_player_to_buyer(player, seller, processor, update_df):
    potential_output = processor.output_payload
    seller.purchase_from_vendor(player, update_df)
    processor.collect_output_payload()
    
######################################################


######################################################
###Player
#A vendor will be put aside for the player
#The player will be able to buy any item and will essentially have a "sell only" catalogue
#may need to place an override to the player restrictions on matching inventory
#Actions the player performs will place items in their inventory, buy/sell, or move on grid
def create_player():
    player = vendors.Vendor(
        vendor_name = "Player 1",
        vendor_type = "Both",
        account = accounts.MoneyAccount(),
            )
    player.account.set_balance(10000)
    return player
######################################################


######################################################
###Machine
def generate_new_machine(update_df):
    
    machine_identity_info = list(update_df[[
                             'product_type',
                             'form',
                             'potency',
                             'process_time'
                             ]].values[0])
    #Need to input machine abilities here
    #Most notable is the shape of each machine
    #TODO: Finish look-up dictionaries for each machine type
    #create look-up dictionaries based on attributes
    #capacity
    shape = {1:[[1]],
             3:[[1,1], [1,1]],
             5:[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]}
    processible_inputs = {"Testulator" : ["Testonium"],
                          "Exbopulator" : ["Experimentallite"],
                          "Pilomatic" : ["Pilotine"]}
    capacity = {"Testulator" : 20,
                "Exbopulator" : 30,
                "Pilomatic" : 40}
    
    new_machine = machines.MachineUnit(
    cost = update_df["cost"].iloc[0],
    shape = shape[machine_identity_info[3]],
    owner = "Player 1",
    machine_name = update_df["product_type"].iloc[0],
    processable_inputs = processible_inputs[update_df["product_type"].iloc[0]],
    augment = update_df["form"].iloc[0],
    augment_potency = update_df["potency"].iloc[0],
    capacity = capacity[update_df["product_type"].iloc[0]],
    turns_to_process = update_df["process_time"].iloc[0])
    
    return new_machine



######################################################

######################################################
###Machine
def generate_new_processor(new_machine):
    
    new_processor = processors.ProcessorUnit(mechanism = new_machine)
    
    return new_processor
######################################################



def generate_new_payload(update_df):
    
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
"""    
    shape = {1:[[1]],
             3:[[1,1], [1,1]],
             5:[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]}
    processible_inputs = {"Testulator" : ["Testonium"],
                          "Exbopulator" : ["Experimentallite"],
                          "Pilomatic" : ["Pilotine"]}
    capacity = {"Testulator" : 20,
                "Exbopulator" : 30,
                "Pilomatic" : 40}
    
    new_machine = machines.MachineUnit(
    cost = update_df["cost"].iloc[0],
    shape = shape[machine_identity_info[3]],
    owner = "Player 1",
    machine_name = update_df["product_type"].iloc[0],
    processable_inputs = processible_inputs[update_df["product_type"].iloc[0]],
    augment = update_df["form"].iloc[0],
    augment_potency = update_df["potency"].iloc[0],
    capacity = capacity[update_df["product_type"].iloc[0]],
    turns_to_process = update_df["process_time"].iloc[0])
    
    return new_machine
"""