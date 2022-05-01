# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:33:15 2022

@author: Kyle Stanley

This test the core machine logic.  This will test the attributes of each
machine and the ability to change these attributes.
"""

from source_indufin_game import machines


def test_machine_object_shape():
    """Tests basics of account creation"""

    basic_machine = machines.CreatedMachine()
    assert basic_machine
    assert basic_machine.cost == 0
    assert basic_machine.size == 1
    assert basic_machine.shape == [1]
    assert basic_machine.owner == "None Assigned"
    assert basic_machine.machine_name == "Generic Machine"
    assert basic_machine.processable_inputs == set(["None"])
    assert basic_machine.augment == "No Augmentation"
    assert basic_machine.augment_potency == 0

    basic_machine = machines.CreatedMachine(
        cost = 100,
        shape = [1, 1, 1, 1, 1],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)
    assert basic_machine.cost == 100
    assert basic_machine.size == 5
    assert basic_machine.owner == "Player 1"
    assert basic_machine.machine_name == "Testulator"
    assert basic_machine.processable_inputs == set(["Testonium",
                                                    "Testadon"])
    assert basic_machine.augment == "Melt"
    assert basic_machine.augment_potency == 3


def test_machine_altering_shape():
    """Tests basics of account creation"""

    basic_machine = machines.CreatedMachine(
        cost = 100,
        shape = [1, 1, 1, 1, 1],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)

    basic_machine.set_cost(10)
    basic_machine.set_owner("Player 2")
    basic_machine.set_shape([1, 1, 1])
    basic_machine.set_machine_name("Retestulator")
    basic_machine.set_processable_inputs(["Retestonium", "Retestadon"])
    basic_machine.set_augment("Strengthen")
    basic_machine.set_augment_potency(5)

    assert basic_machine.cost == 10
    assert basic_machine.size == 3
    assert basic_machine.owner == "Player 2"
    assert basic_machine.machine_name == "Retestulator"
    assert basic_machine.processable_inputs ==  set(["Retestonium",
                                                     "Retestadon"
                                                     ])
    assert basic_machine.augment == "Strengthen"
    assert basic_machine.augment_potency == 5

    basic_machine.add_processable_input("Testanium")
    assert basic_machine.processable_inputs ==  set(["Retestonium",
                                                 "Retestadon",
                                                 "Testanium"
                                                 ])

    basic_machine.remove_processable_input("Testanium")
