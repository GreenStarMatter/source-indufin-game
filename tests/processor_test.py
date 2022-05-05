# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:02:42 2022

@author: Kyle Stanley
"""


from source_indufin_game import processors
from source_indufin_game import machines
from source_indufin_game import materials


def test_processor_object_shape():
    """Basic form test of processor"""

    basic_processor = processors.ProcessorUnit()
    assert basic_processor.mechanism
    assert basic_processor.input_payload
    assert basic_processor.turns_to_produce == 0


    basic_machine = machines.MachineUnit()
    basic_material = materials.MaterialUnit()
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        input_payload = basic_material,
        turns_to_produce = 1
        )
    assert basic_processor

def test_processor_altering():
    """Test basic altering of class"""

    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5,
        capacity = 30)
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        input_payload = [basic_material, 20],
        turns_to_produce = 1
        )

    assert basic_processor.output_payload.material_name \
        == "Testonium"
    assert basic_processor.output_payload.form \
        == "Melted"
    assert basic_processor.output_payload.form_potency \
        == 5
    assert basic_processor.output_payload.owner \
        == "Player 1"
    assert basic_processor.output_payload.cost \
        == 100


def test_processor_what_if_new_material():
    """Test what a new material is added to processor"""

    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        turns_to_produce = 1
        )
    material_amount = 20
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor.set_payload([basic_material, material_amount])

    assert basic_processor.output_payload.material_name \
        == "Testonium"
    assert basic_processor.output_payload.form \
        == "Melted"
    assert basic_processor.output_payload.form_potency \
        == 5
    assert basic_processor.output_payload.owner \
        == "Player 1"
    assert basic_processor.output_payload.cost \
        == 100


def test_processor_what_if_new_mechanism():
    """Test what a new mechanism is added to processor"""

    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor = processors.ProcessorUnit(
        input_payload = basic_material,
        turns_to_produce = 1
        )
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5)
    basic_processor.set_mechanism(basic_machine)

    assert basic_processor.output_payload.material_name \
        == "Testonium"
    assert basic_processor.output_payload.form \
        == "Melted"
    assert basic_processor.output_payload.form_potency \
        == 5
    assert basic_processor.output_payload.owner \
        == "Player 1"
    assert basic_processor.output_payload.cost \
        == 100
