# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:38:07 2022

@author: Kyle Stanley
"""

import string
import os
import datetime
import time
import pandas as pd
from source_indufin_game import vendors
from source_indufin_game import accounts
from source_indufin_game import machines
from source_indufin_game import materials
from source_indufin_game import grid
from source_indufin_game import processors

############################################################################
###Gameflow helper functions
def win_condition_check(win_threshold, player):
    """Determine whether or not player has achieved win condition."""

    win_condition = win_threshold <= player.account.balance
    if win_condition:
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
        print("!!!  WINNER !!!")
    return win_condition


def evaluate_quit(player_input):
    """Evaluate player quit input.  Give verification opportunity."""

    player_quit = False
    if player_input == "quit":
        player_input = input("Are you sure, all progress will be lost?" +
                             " (y) to quit\n>>>>>")
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

    return update_df["stock"].values[0] >= stock_check_value\
        and stock_check_value != 0
def get_matching_player_stock_from_update(update_df, player):
    """Return player stock for item"""

    player_stock = 0
    player.sale_is_possible(update_df)
    return player_stock


def print_vendor_for_ux(vendor):
    """Pretty print of vendor data so user can browse catalogue"""

    print(f"\n***{vendor.vendor_name}***\n")
    print(vendor.catalogue)

def get_all_available_machines_for_placement(grid,
                                             processors_available):
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
        print(f"Location: {grid.objects_on_grid[machine]}")
        print(f"{mach_ind} : {machine.machine_name} : {availability}")
        print(machine.__str__())
        print("*****************************************\n")

def get_all_available_machines_for_placement_in_queue(
        grid, processors_available, queue):
    """Pretty print of all machines and the index to select them.  Also shows
    if the machine is ready to accept a new payload"""

    all_machines = list(grid.objects_on_grid.keys())
    all_available_machines = [machine for machine\
                              in all_machines\
                                      if machine not in queue]
    for mach_ind, machine in enumerate(all_available_machines):
        processor = processors_available[machine]
        machine_available = (processor.output_payload is None)\
            and (processor._processing_flag == 0)
        availability = "Processing"
        if machine_available:
            availability = "Available"
        print("*****************************************")
        print(f"Location: {grid.objects_on_grid[machine]}")
        print(f"{mach_ind} : {machine.machine_name} : {availability}")
        print(machine.__str__())
        print("*****************************************\n")


def get_all_available_materials_for_placement(start_ind_of_materials,
                                              all_ready_processors):
    """Pretty print of all materials which are ready for harvesting."""

    for processor_ind, processor in enumerate(all_ready_processors):
        output_payload = processor.output_payload
        print("*****************************************")
        print(f"{start_ind_of_materials + processor_ind} :"+
              f" {output_payload[0].material_name} {output_payload[0].form}"+
              f" {output_payload[0].form_potency}: {output_payload[1]}")
        print("*****************************************\n")


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


def print_pretty_player_catalogue(player):
    """Hides None row if player has items in catalogue"""

    if len(player.catalogue["product_type"].values) >= 2:
        print(player.catalogue[player.catalogue["product_type"] != "None"])
    else:
        print(player.catalogue)

def convert_coordinates_to_tuple(coordinate_string):
    """Converts input string of the form xy into a coordinate tuple"""

    return (int(coordinate_string[0]), int(coordinate_string[1]))

def print_machine_attributes_of_seller_catalogue():
    """Prints detailed attributes of all machines."""

    shape_size_lookup = {("Testulator", 5) : 1,
                         ("Exbopulator", 12) : 1,
                         ("Pilomatic", 50) : 1,
                         ("Testulator", 25) : 2,
                         ("Exbopulator", 50) : 2,
                         ("Pilomatic", 100) : 2,
                         ("Testulator", 100) : 3,
                         ("Exbopulator", 200) : 3,
                         ("Pilomatic", 150) : 3
                         }
    shape_lookup = {1:[[1]],
                    2:[[1,1], [1,1]],
                    3:[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]}
    processible_inputs = {"Testulator" : ["Testonium"],
                          "Exbopulator" : ["Experimentallite"],
                          "Pilomatic" : ["Pilotine"]}

    for specific_machine_config in shape_size_lookup.keys():
        print("____________________\n")
        print(f"{specific_machine_config[0]} {specific_machine_config[1]}")
        print_load = "".join(["|"+ " ".join([str(element) for element in row])\
                              + "|\n" for row in\
                                  shape_lookup[
                                      shape_size_lookup[
                                          specific_machine_config]]])
        print(print_load[:-1])
        print(f"Processes {'|'.join(processible_inputs[specific_machine_config[0]])}")
        print("--------------------\n")

def append_item_to_ledger(
        ledger, origin, end, item, amount, line_id, transaction_id):
    """Appends a new line to the ledger"""

    ledger_columns = ["From", "To", "Item",
                      "Amount", "Line_ID", "Transaction_ID"]
    new_ledger_line = [[origin, end, item, amount, line_id, transaction_id]]
    ledger_line = pd.DataFrame(new_ledger_line, columns = ledger_columns)
    ledger = pd.concat([ledger, ledger_line])
    return ledger



def execute_ledger_transaction(ledger, ledger_items, line_id, transaction_id):
    """Executes a batch of appends to the ledger as a transaction"""

    for ledger_update in ledger_items:
        origin = ledger_update[0]
        end = ledger_update[1]
        item = ledger_update[2]
        amount = ledger_update[3]
        ledger = append_item_to_ledger(
            ledger, origin, end, item, amount, line_id, transaction_id)
        line_id += 1
    transaction_id += 1
    return ledger, line_id, transaction_id

def write_ledger_to_output_file(ledger):
    """Index for session retrieval"""
    #give filepath
    #write ledger
    cwd = os.getcwd()
    subfolder_path = (r"analysis\session_data")
    full_path_to_folder = os.path.join(cwd,subfolder_path)
    current_timestamp = time.time()
    index_no = str(len(os.listdir(full_path_to_folder)))
    complete_time =\
        datetime.datetime.fromtimestamp(current_timestamp)\
            .strftime('%Y_%m_%d__%H_%M_%S')
    file_name = f"TransactionLog{index_no}_{complete_time}.csv"
    ledger_write_path = os.path.join(full_path_to_folder, file_name)
    ledger.to_csv(ledger_write_path, index = False)


def print_basic_tutorial_help_information(starting_capital, win_threshold):
    """Prints help information.  This contains the information needed to
    play the game."""

    print("\n\n\n")
    print(f"""Hello, welcome to the source-indufin game!\n
          Currently you are in a basic tutorial mode.  You have been given
          ${starting_capital} to start.  Your objective is to raise more
          than ${win_threshold}.  You can do this by purchasing
          materials and machines, running a factory, and selling processed
          materials.\n\nThe actions you can perform are:
          
          BUY: Purchase machines or materials so you can place them in your
          factory.
          SELL: Sell machines or processed materials to make money.
          PLACE IN FACTORY:  Place machines on factory floor grid or place
          materials in available machines
          REMOVE FROM FACTORY: Remove materials or machines from factory
           floor.
          END TURN: End the day and allow machines to process materials.
          
          
          A normal progression would be to:
          1. Buy a machine from a seller
          2. Buy material which matches the machine input payload
          3. Place the machine in your factory
          4. Place the material in your factory
          5. Pass turns until the material is ready to be harvested
          6. Harvest material into your catalogue
          7. Sell material to buyer
          8. Determine how to spend your profit!
          
          
          Bonus actions can be performed to make turns more efficient:
              
          - Harvest All Machines allows the player to automatically harvest all
          machines which have fully processed materials instead of having to
          individually pull from each one.
          - Set Priority Queue allow the player to arrange machines on the grid
          so that they can be autofilled.
          - Autofill Priority Queue automatically allocates materials to
          machines based on how the player previously set-up.
          
          These 3 actions are very helpful for mature factories.  For example,
          a factory with 10 machines would take approximately 80 commands to
          process.  However, this can be minimized to just 3 top level options.
          
          """)
    print("\n\n\n")
    input("Press Enter to Continue\n\n")


def insert_item_to_priority_queue(queue, item_to_insert,
                                  position, above_below):
    """Insert an item in the priorty queue based on user preference.
    Orientation was chosen to align with what the user is displayed on the
    screen."""

    if queue:
        position_modifier = 0
        if above_below == "b":
            position_modifier = 1
        elif above_below == "a":
            position_modifier = 0
        else:
            print("Invalid Token")
        queue.insert(position + position_modifier, item_to_insert)
    else:
        queue.append(item_to_insert)

def remove_item_from_priority_queue(queue, position):
    """Remove an item from the priority queue by index"""
    queue.pop(position)

def pretty_print_priority_queue(queue, processors_available, grid):
    """Clean print of the priority queue for user reading."""

    if not queue:
        print("\n\nCurrently no items in queue\n\n")
    for mach_ind, machine in enumerate(queue):
        processor = processors_available[machine]
        if machine in queue:
            machine_available = (processor.output_payload is None)\
                and (processor._processing_flag == 0)
            availability = "Processing"
            if machine_available:
                availability = "Available"
            print("*****************************************")
            print(f"Location: {grid.objects_on_grid[machine]}")
            print(f"{mach_ind} : {machine.machine_name} : {availability}")
            print(machine.__str__())
            print("*****************************************\n")

def clean_up_queue(queue, processors_available):
    """Removes items from queue that are no longer on grid."""

    cleaned_queue = []
    for machine in queue:
        if machine in processors_available.keys():
            cleaned_queue.append(machine)
        else:
            print(f"{machine.machine_name} {machine.capacity} at " +\
                  "removed from queue")

    return cleaned_queue
   

def auto_fill_priority_queue_items(
        queue, player, processors_available, factory):
    """Automatically fills all machines in priority queue.  If there is not
     enough materials to fill then the machine will be skipped.
    Need to update machine processable_inputs.  It only looks
     at material name right now and it should also see augment and potency
     big change which is touched by multiple classes.
     LUCKILY, since this is the tutorial all of the inputs are 0 and I can
     shortcut the autofill instead of doing a look-up"""

    avail = lambda x: (x.output_payload is None) and (x._processing_flag == 0)
    all_available_machines = [machine for machine\
                              in queue if avail(processors_available[machine])]
    for machine in all_available_machines:
        player_input_coordinates_of_machine = factory.objects_on_grid[machine]
        material_name = list(machine.processable_inputs)[0]
        capacity = machine.capacity

        temp_catalogue = player.catalogue.copy()
        catalogue_row = temp_catalogue[
            (temp_catalogue["product_type"] == material_name) &
            (temp_catalogue["form"] == "Bar") &
            (temp_catalogue["potency"] == 0)].copy()
        update_amount = min(capacity, catalogue_row["stock"].iloc[0])
        update_df = create_material_placement_update_df(
            catalogue_row, update_amount)
        if update_amount>0:
            move_material_from_player_catalogue_to_machine(
                player, factory, processors_available,
                update_df, player_input_coordinates_of_machine)
        else:
            print("Not enough stock for auto-fill")
        #check catalogue, check capacity
############################################################################

############################################################################
###Asset creation functions
#Priority Queue
def create_priority_queue():
    return []

#Ledger
def create_ledger():
    """Creates a transactional ledger for storing transaction of assets."""

    ledger_columns = ["From", "To", "Item",
                      "Amount", "Line_ID", "Transaction_ID"]
    new_ledger_line = [["VOID", "Game", "New Session", 1, 0, 0]]
    new_ledger = pd.DataFrame(new_ledger_line, columns = ledger_columns)
    return new_ledger

#Buyer
def create_buyer_vendor():
    """Creates buyer vendor."""

    vendor_columns = ["vendor_type", "product_type", "form",
                      "potency", "stock", "cost", "process_time", "capacity"]
    buyer_catalogue = [["Buy", "Testonium", "Melted", 3, 0, 8, -1, -1]]
    buyer_catalogue.append(["Buy", "Experimentallite",
                            "Melted", 3, 0, 6, -1, -1])
    buyer_catalogue.append(["Buy", "Pilotine", "Melted", 3, 0, 4, -1, -1])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 30, 1, 5])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 150, 1, 25])
    buyer_catalogue.append(["Buy", "Testulator", "Melt", 3, 0, 600, 1, 100])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 24, 2, 12])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 100, 2, 50])
    buyer_catalogue.append(["Buy", "Exbopulator", "Melt", 3, 0, 400, 2, 200])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 34, 3, 50])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 67, 3, 100])
    buyer_catalogue.append(["Buy", "Pilomatic", "Melt", 3, 0, 100, 3, 150])
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
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 50, 60, 1, 5])
    seller_catalogue.append(["Sell", "Testulator", "Melt", 3, 25, 300, 1, 25])
    seller_catalogue.append(["Sell", "Testulator", "Melt",
                             3, 5, 1200, 1, 100])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 50, 48, 2, 12])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt", 3, 25, 200, 2, 50])
    seller_catalogue.append(["Sell", "Exbopulator", "Melt",
                             3, 5, 800, 2, 200])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 50, 67, 3, 50])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 25, 134, 3, 100])
    seller_catalogue.append(["Sell", "Pilomatic", "Melt", 3, 5, 200, 3, 150])
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
    shape_size_lookup = {("Testulator", 5) : 1,
                         ("Exbopulator", 12) : 1,
                         ("Pilomatic", 50) : 1,
                         ("Testulator", 25) : 2,
                         ("Exbopulator", 50) : 2,
                         ("Pilomatic", 100) : 2,
                         ("Testulator", 100) : 3,
                         ("Exbopulator", 200) : 3,
                         ("Pilomatic", 150) : 3
                         }
    shape_size  = shape_size_lookup[(machine_identity_info[0],
                                     machine_identity_info[4])]
    shape_lookup = {1:[[1]],
                    2:[[1,1], [1,1]],
                    3:[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]}
    processible_inputs = {"Testulator" : ["Testonium"],
                          "Exbopulator" : ["Experimentallite"],
                          "Pilomatic" : ["Pilotine"]}

    new_machine = machines.MachineUnit(
    cost = update_df["cost"].iloc[0],
    shape = shape_lookup[shape_size],
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

    transaction_cost = str(update_df["stock"].iloc[0] *\
                           update_df["cost"].iloc[0])
    item = "|".join([update_df["product_type"].iloc[0],
                     update_df["form"].iloc[0],
                     str(update_df["potency"].iloc[0]),
                     str(update_df["capacity"].iloc[0])])
    ledger_items = [["Seller", "Player",
                     item, str(update_df["stock"].iloc[0])],
                    ["Seller", "Player",
                     "Capital", transaction_cost]
                    ]
    global ledger
    global transaction_id
    global line_id
    ledger, line_id, transaction_id  =\
            execute_ledger_transaction(ledger, ledger_items,
                                       line_id, transaction_id)

    player.purchase_from_vendor(seller, update_df)
    player.catalogue["vendor_type"] = "Sell"


def move_item_from_player_to_buyer_catalogue(player, buyer, update_df):
    """Transacts a sale to a buyer from the player"""

    transaction_cost = str(update_df["stock"].iloc[0] *\
                           update_df["cost"].iloc[0])
    item = "|".join([update_df["product_type"].iloc[0],
                     update_df["form"].iloc[0],
                     str(update_df["potency"].iloc[0]),
                     str(update_df["capacity"].iloc[0])])
    ledger_items = [["Player", "Buyer",
                     item, str(update_df["stock"].iloc[0])],
                    ["Player", "Buyer",
                     "Capital", transaction_cost]
                    ]
    global ledger
    global transaction_id
    global line_id
    ledger, line_id, transaction_id  =\
            execute_ledger_transaction(ledger, ledger_items,
                                       line_id, transaction_id)

    buyer.purchase_from_vendor(player, update_df)
    player.catalogue["vendor_type"] = "Sell"

def move_machine_from_player_catalogue_to_grid(player,
                                               factory,
                                               processors_available,
                                               update_df,
                                               coordinates):
    """Transacts a machine out of the players catalogue and places it on
    the grid.  Creates a processor corresponding to the machine as well."""

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
        item = "|".join(["".join([str(a) for a in coordinates]),
                         update_df["product_type"].iloc[0],
                         update_df["form"].iloc[0],
                         str(update_df["potency"].iloc[0]),
                         str(update_df["capacity"].iloc[0])])
        ledger_items = [["Player", "Grid",
                         item, 1]]
        global ledger
        global transaction_id
        global line_id
        ledger, line_id, transaction_id  =\
                execute_ledger_transaction(ledger, ledger_items,
                                           line_id, transaction_id)
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
        item = "|".join(["".join([str(a) for a\
                                  in player_input_coordinates_of_machine]),
                         update_df["product_type"].iloc[0],
                         update_df["form"].iloc[0],
                         str(update_df["potency"].iloc[0])])
        ledger_items = [["Player", "Grid",
                         item, str(update_df["stock"].iloc[0])]]
        global ledger
        global transaction_id
        global line_id
        ledger, line_id, transaction_id  =\
                execute_ledger_transaction(ledger, ledger_items,
                                           line_id, transaction_id)
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
        update_columns = ["vendor_type", "product_type", "form", "potency",
                          "stock", "cost", "process_time", "capacity"]
        catalogue_update = [["Sell", output_payload[0].material_name,
                             output_payload[0].form,
                            output_payload[0].form_potency, output_payload[1],
                            0, -1, -1]]
        update_df = pd.DataFrame(catalogue_update, columns = update_columns)
        item = "|".join([update_df["product_type"].iloc[0],
                         update_df["form"].iloc[0],
                         str(update_df["potency"].iloc[0])])
        ledger_items = [["Grid", "Player",
                         item, str(update_df["stock"].iloc[0])]]
        global ledger
        global transaction_id
        global line_id
        ledger, line_id, transaction_id  =\
                execute_ledger_transaction(ledger, ledger_items,
                                           line_id, transaction_id)
        player.update_catalogue("Purchase", update_df)

    return valid_transaction


def move_machine_from_grid_into_player_catalogue(
        player, factory, processors_available,
        player_input_coordinates_to_transform, update_df):
    """Transacts a machine from the grid back into a player's catalogue"""

    transaction_valid = False
    easy_index_items = \
        index_all_grid_machines_for_player_readability(factory)

    transaction_gate_1 =\
        player_input_coordinates_to_transform in easy_index_items.keys()

    if transaction_gate_1:

        item = "|".join(["".join([str(a) for a\
                                  in player_input_coordinates_to_transform]),
                         update_df["product_type"].iloc[0],
                         update_df["form"].iloc[0],
                         str(update_df["potency"].iloc[0]),
                         str(update_df["capacity"].iloc[0])])
        ledger_items = [["Grid", "Player",
                         item, 1]]
        global ledger
        global transaction_id
        global line_id
        ledger, line_id, transaction_id  =\
                execute_ledger_transaction(ledger, ledger_items,
                                           line_id, transaction_id)
        transaction_valid = True
        object_to_remove = easy_index_items[
        player_input_coordinates_to_transform
        ][2]

        player.update_catalogue("Purchase", update_df)
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
        amount_prompt = "Select item amount or (m) for main menu:\n>>>>>"
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


def player_decision_choose_quantity_to_sell(player, buyer, catalogue_row):
    """Takes player input to get the quantity of the item being sold"""

    player_input_catalogue_check_valid = False
    while not player_input_catalogue_check_valid:
        amount_prompt = "Select item amount or (m) for main menu:\n>>>>>"
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


def player_decision_seller_catalogue_branch(player, seller):
    """Takes player input to decide which item in seller catalogue will be
     purchased"""

    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu or "+\
            "(e) to examine machines:\n>>>>>"
        player_input = input(item_prompt)
        if (not player_input.isdigit()) and (player_input != "m")\
            and (player_input != "e"):
            print("Input invalid, please try again.")
        elif player_input == "m":
            player_input_check_valid_item = True
        elif player_input == "e":
            print_machine_attributes_of_seller_catalogue()
        elif int(player_input) in seller.catalogue.index:
            player_input = int(player_input)
            catalogue_row = seller.catalogue.loc[[player_input]]
            player_decision_choose_quantity_to_purchase(player, seller,
                                                        catalogue_row)
            player_input_check_valid_item = True
        else:
            print("Input invalid, please try again.")


def player_decision_buyer_catalogue_branch(player, buyer):
    """Takes player input to decide which item in buyer catalogue will be
     sold"""

    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu:\n" +\
            ">>>>>"
        player_input = input(item_prompt)
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


def player_decision_buy_or_sell_branch(player, buyer, seller):
    """Takes player input whether the player wants to interact with a buyer or
    with a seller"""

    valid_buy_sell = False
    while not valid_buy_sell:
        buy_sell_prompt = "Enter 1 to buy, 2 to sell, " +\
            "(m) to return to main menu:\n>>>>>"
        player_input = input(buy_sell_prompt)

        if player_input == "1":
            valid_buy_sell = True
            print_vendor_for_ux(seller)
            player_decision_seller_catalogue_branch(player, seller)
        elif player_input == "2":
            valid_buy_sell = True
            print_pretty_player_catalogue(player)
            print_vendor_for_ux(buyer)
            player_decision_buyer_catalogue_branch(player, buyer)
        elif player_input == "m":
            valid_buy_sell = True
        else:
            print("Input invalid, please try again.")


def player_decision_validate_overwrite_existing():
    player_decided_to_overwrite = False
    player_input_machine = input("Overwrite existing load?  This will destroy"+
                                 "the output as well: (y)/(n)\n>>>>>")

    if player_input_machine == "y":
        player_decided_to_overwrite = True
    elif player_input_machine == "n":
        print("Overwrite aborted.")
    else:
        print("Input invalid, please try again.")

    return player_decided_to_overwrite


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
                                                 processors_available)
        machine_choice_prompt = "Choose the index of a machine to place"+\
            " material in or (m) for main menu: "
        material_amount_prompt = "Choose the amount to place in machine:\n" +\
            ">>>>>"
        player_input_machine = input(machine_choice_prompt)
        if material_amount_prompt == "m":
            player_input_amount = 0
        else:
            player_input_amount = input(material_amount_prompt)

        if (not player_input_machine.isdigit())\
            and (player_input_machine != "m")\
                or (not player_input_amount.isdigit()):
            print("Input invalid, please try again.")
        elif player_input_machine == "m":
            player_input_to_choose_machine_valid = True
        elif int(player_input_machine)>len(all_machines_on_grid) or\
            int(player_input_machine)<0:
            print("Input invalid, please try again.")
        else:
            machine = all_machines_on_grid[int(player_input_machine)]
            define_output_payload = False
            if processors_available[machine]._processing_flag:
                define_output_payload =\
                    player_decision_validate_overwrite_existing()
            else:
                define_output_payload = True
            if define_output_payload:
                player_input_to_choose_machine_valid = True
                player_input_coordinates_of_machine = grid.objects_on_grid[machine]
                update_df =\
                    create_material_placement_update_df(catalogue_row,
                                                        int(player_input_amount))
                if player.sale_is_possible(update_df):
                    player_input_to_choose_machine_valid =\
                        move_material_from_player_catalogue_to_machine(
                            player, grid, processors_available,
                            update_df, player_input_coordinates_of_machine)
                else:
                    print("Not enough stock")

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


def player_decision_player_catalogue_branch(player,
                                            processors_available,
                                            grid):
    """Player input decision to choose an item from own catalogue to place on
    grid"""

    player_input_check_valid_item = False
    while not player_input_check_valid_item:
        item_prompt = "Select item # from catalogue or (m) for main menu:\n"+\
            ">>>>>"
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
                                             processors_available)
        get_all_available_materials_for_placement(start_ind_of_materials,
                                                  all_ready_processors)

        player_input = input("Select object for removal\n>>>>>")
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
            machine_okay_to_remove =\
                player_input_verify_machine_removal(machine, processors_available)
            if machine_okay_to_remove:
                player_input_check_valid_item =\
                    move_machine_from_grid_into_player_catalogue(
                        player, grid, processors_available,
                        machine_coords, update_df)
            else:
                player_input_check_valid_item = True
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
                "Select (m) to go to main menu\n>>>>>"
        player_input = input(player_input_grid_options)
        if player_input == "1":
            print_pretty_player_catalogue(player)
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

def player_decision_harvest_all_materials(player, processors_available):
    """Auto-Harvests all available materials.  Does so by looking through all
    processors with a high payload ready flag and prints results."""

    processors_with_payload = [processor for processor in \
                               processors_available.values() if \
                                   processor.output_payload_ready_flag == 1]
    if processors_with_payload:
        print("000000000000000000000000000000000000000000000000000000")
        print("Harvested")
        for processor in processors_with_payload:
            print("---------")
            print(f"{processor.output_payload}")
            print("---------")
            move_material_in_processor_into_player_catalogue(player, processor)
        print("000000000000000000000000000000000000000000000000000000")
    else:
        print("No processors had output payloads.")

def player_decision_priority_queue_branch(
        queue, processors_available, factory):
    pretty_print_priority_queue(queue, processors_available, factory)
    player_input_valid = False

    while not player_input_valid:
        queue_decision = input("Select 1 to move new item into the queue\n" +\
                               "Select 2 to remove an item from the queue.\n"+\
                                   "Select (m) to return to main menu\n>>>>>")
        if queue_decision == "1":
            player_input_valid = True
            player_decision_priority_queue_insert_item_branch(
                queue, processors_available, factory)
        elif queue_decision == "2":
            player_input_valid = True
            player_decision_priority_queue_remove_item(
                queue, processors_available, factory)
        elif queue_decision == "m":
            player_input_valid = True
        else:
            print("Input invalid, please try again.")

def player_decision_priority_queue_choose_insert_poistion(
        queue, processors_available, factory, item_to_insert):
    player_input_valid = False

    while not player_input_valid:
        pretty_print_priority_queue(queue, processors_available, factory)
        queue_decision = input("Select position to insert into queue\n" +\
                               "Select (m) to return to main menu\n>>>>>")
        if (not queue_decision.isdigit()) and (queue_decision != "m"):
            print("Input invalid, please try again.")
        elif queue_decision == "m":
            player_input_valid = True
        elif int(queue_decision)>=0 and int(queue_decision)<len(queue):
            player_ab_valid = False
            while not player_ab_valid:
                ab_decision = input("Select (a) above or (b) below \n" +\
                                       "Select (m) to return to main menu\n"+\
                                           ">>>>>")
                if ab_decision == "a" or ab_decision == "b":
                    insert_item_to_priority_queue(queue, item_to_insert,
                                  int(queue_decision), ab_decision)
                    player_ab_valid = True
                    player_input_valid = True
                elif ab_decision == "m":
                    player_ab_valid = True
                    player_input_valid = True
                else:
                    print("Input invalid, please try again.")
        else:
            print("Input invalid, please try again.")

def player_decision_priority_queue_insert_item_branch(
        queue, processors_available, factory):
    player_input_valid = False

    all_available_machines = [machine for machine\
                              in list(factory.objects_on_grid.keys())\
                                      if machine not in queue]
    while not player_input_valid:
        get_all_available_machines_for_placement_in_queue(
            factory, processors_available, queue)
        queue_decision = input("Select item index to add to queue\n" +\
                               "Select (m) to return to main menu\n>>>>>")
        pretty_print_priority_queue(queue, processors_available, factory)
        if (not queue_decision.isdigit()) and (queue_decision != "m"):
            print("Input invalid, please try again.")
        elif queue_decision == "m":
            player_input_valid = True
        elif int(queue_decision)>=0\
            and int(queue_decision)<len(all_available_machines):
            player_input_valid = True
            if queue:
                player_decision_priority_queue_choose_insert_poistion(
                        queue,
                        processors_available,
                        factory,
                        all_available_machines[int(queue_decision)])
            else:
                insert_item_to_priority_queue(
                    queue, all_available_machines[int(queue_decision)],
                    0, "a")
        else:
            print("Input invalid, please try again.")

def player_decision_priority_queue_remove_item(
        queue, processors_available, factory):
    player_input_valid = False

    while not player_input_valid:
        pretty_print_priority_queue(queue, processors_available, factory)
        queue_decision = input("Select item index to remove from queue\n" +\
                               "Select (m) to return to main menu\n>>>>>")
        if (not queue_decision.isdigit()) and (queue_decision != "m"):
            print("Input invalid, please try again.")
        elif queue_decision == "m":
            player_input_valid = True
        elif int(queue_decision)>=0 and int(queue_decision)<len(queue):
            remove_item_from_priority_queue(queue, int(queue_decision))
            print("\n\nItem successfully removed, remove another?\n\n")
        else:
            print("Input invalid, please try again.")


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
            "placement (xy)\nSelect (m) to return to main menu\n>>>>>"
        player_input = input(player_input_grid_placement_string)

        if player_input == "m":
            transaction_completed = True
        elif len(player_input) != 2:
            print("Input invalid, please try again.")
        elif player_input[0].isdigit() and player_input[1].isdigit():
            input_coordinates =\
                convert_coordinates_to_tuple(player_input)
            update_df = catalogue_row.copy()
            update_df["stock"] = 1
            if player.sale_is_possible(update_df):
                transaction_completed =\
                    move_machine_from_player_catalogue_to_grid(
                    player, grid, processors_available,
                    update_df, input_coordinates)
            else:
                transaction_completed = True
                print("\nNo machines to place, returning to main menu")
        else:
            print("Input invalid, please try again.")

def player_input_verify_machine_removal(machine, processors_available):
    """Verify with player if machine contains a material.  This is to avoid
    accidentally destroying resources."""

    machine_okay_to_remove = False
    #while 1:
    if processors_available[machine].output_payload:
        valid_removal_decision = False
        while not valid_removal_decision:
            player_input = input(">>>>>\nMachine is currently processing, " +
                                 "removal will destroy in process material " +
                                 "(p) to proceed, (a) to abort")
            if player_input == "p":
                valid_removal_decision = True
                machine_okay_to_remove = True
                print("Proceeding with removal")
            elif player_input == "a":
                valid_removal_decision = True
                print("Aborting removal")
            else:
                print("Input invalid, please try again.")
    else:
        machine_okay_to_remove = True
    return machine_okay_to_remove
############################################################################


def basic_tutorial_game():
    """Play flow logic for basic game.  Win condition is a simple threshold."""

    global ledger
    global transaction_id
    global line_id
    transaction_id = 1
    line_id = 1
    ledger = create_ledger()
    win_threshold = 3500
    starting_capital = 275
    turn_counter = 0
    buyer = create_buyer_vendor()
    seller = create_seller_vendor()
    player = create_player(starting_capital)
    factory = create_factory_grid()
    priority_queue = create_priority_queue()
    ledger_items = [["VOID", "Game", "Buyer", 1],
                    ["VOID", "Game", "Seller", 1],
                    ["VOID", "Game", "Player", 1],
                    ["Game", "Player", "Capital", starting_capital],
                    ["VOID", "Game", "Factory", 1]]
    ledger, line_id, transaction_id  =\
        execute_ledger_transaction(ledger, ledger_items, line_id, transaction_id)
    processors_available = {}
    win_condition_met = False
    player_quit = False
    top_level_player_options = ["Buy/Sell",
                                "Place/Move Item",
                                "Harvest All Materials",
                                "Set Priority Queue",
                                "Autofill Priority Queue",
                                "List Machine Configs",
                                "Help",
                                "End Day"]
    quit_string = "\n(quit) to quit game"
    print_basic_tutorial_help_information(starting_capital, win_threshold)
    print("*********************************************************")
    while not (win_condition_met or player_quit):
        print(f"Day {turn_counter}")
        print(f"Balance: {player.account.balance}")
        print(factory.__str__())
        print("\n^v^v^v^v^v^v^v^v^v^v^v Current Stock ^v^v^v^v^v^v^v^v^v^v^v")
        print_pretty_player_catalogue(player)
        print("\n\n")
        command_string = \
            enumerate_list_for_clean_print(top_level_player_options)
        print(command_string + quit_string)
        player_input = input("\n\nEnter a commmand:\n>>>>>")
        print("\n\n\n")
        player_quit = evaluate_quit(player_input)
        if player_input == "0":
            player_decision_buy_or_sell_branch(player, buyer, seller)
        elif player_input == "1":
            player_decision_grid_interaction_branch(player,
                                            factory, processors_available)
        elif player_input == "2":
            player_decision_harvest_all_materials(player, processors_available)
        elif player_input == "3":
            player_decision_priority_queue_branch(
                priority_queue, processors_available, factory)
        elif player_input == "4":
            auto_fill_priority_queue_items(
                priority_queue, player, processors_available, factory)
        elif player_input == "5":
            print_machine_attributes_of_seller_catalogue()
        elif player_input == "6":
            print_basic_tutorial_help_information(
                starting_capital, win_threshold)
        elif player_input == "7":
            turn_counter += 1
            decrement_all_processors(processors_available)
        elif player_input == "quit":
            pass
        else:
            print("Input not recognized")
    
        priority_queue = clean_up_queue(priority_queue, processors_available)

        print("\n\n")
        print("*********************************************************")
        win_condition_met = win_condition_check(win_threshold, player)
    write_ledger_to_output_file(ledger)
    print("***********************************GAME END"+
          "***********************************")


def main():
    """Runs the basic tutorial game.
    Also sets console pandas print options for better experience."""

    pd.set_option('display.width', 1000)
    pd.set_option('max_columns', None)
    basic_tutorial_game()


if __name__ == "__main__":
    main()
