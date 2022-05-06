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
        input_payload = [basic_material, 0]
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
        capacity = 30,
        turns_to_process = 1)
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        input_payload = [basic_material, 20]
        )

    assert basic_processor.output_payload[0].material_name \
        == "Testonium"
    assert basic_processor.output_payload[0].form \
        == "Melted"
    assert basic_processor.output_payload[0].form_potency \
        == 5
    assert basic_processor.output_payload[0].owner \
        == "Player 1"
    assert basic_processor.output_payload[0].cost \
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
        augment_potency = 5,
        turns_to_process = 1)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine
        )
    material_amount = 20
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor.set_payload([basic_material, material_amount])

    assert basic_processor.output_payload[0].material_name \
        == "Testonium"
    assert basic_processor.output_payload[0].form \
        == "Melted"
    assert basic_processor.output_payload[0].form_potency \
        == 5
    assert basic_processor.output_payload[0].owner \
        == "Player 1"
    assert basic_processor.output_payload[0].cost \
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
        input_payload = [basic_material, 20]
        )
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5,
        capacity = 30,
        turns_to_process = 1)
    basic_processor.set_mechanism(basic_machine)

    assert basic_processor.output_payload is None


def test_invalid_material_payload_to_machine_capacity():
    """Test basic altering of class"""

    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5,
        capacity = 5,
        turns_to_process = 1)
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        input_payload = [basic_material, 20]
        )

    assert basic_processor.output_payload is None


def test_valid_decrement_and_retrieval_logic():
    """Test the decrementing of class down to 0.  At 0 the processor
    is tested whether it can properly retrieve and delete the output payload.
    """

    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1, 1, 1, 1, 1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 5,
        capacity = 5,
        turns_to_process = 3)
    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Raw",
        form_potency = 3)
    basic_processor = processors.ProcessorUnit(
        mechanism = basic_machine,
        input_payload = [basic_material, 5]
        )

    assert basic_processor.turns_to_produce == 3
    assert basic_processor.output_payload[0].material_name \
        == "Testonium"
    assert basic_processor.output_payload[0].form \
        == "Melted"
    assert basic_processor.output_payload[0].form_potency \
        == 5
    assert basic_processor.output_payload[0].owner \
        == "Player 1"
    assert basic_processor.output_payload[0].cost \
        == 100
    assert basic_processor.output_payload[1] \
        == 5
    assert basic_processor.collect_output_payload() is None

    basic_processor.decrement_processor_tracker()
    assert basic_processor.turns_to_produce == 2
    assert basic_processor.collect_output_payload() is None

    basic_processor.decrement_processor_tracker()
    assert basic_processor.turns_to_produce == 1
    assert basic_processor.collect_output_payload() is None

    basic_processor.decrement_processor_tracker()
    assert basic_processor.turns_to_produce == 0

    output_payload = basic_processor.collect_output_payload()
    assert output_payload[0].material_name \
        == "Testonium"
    assert output_payload[0].form \
        == "Melted"
    assert output_payload[0].form_potency \
        == 5
    assert output_payload[0].owner \
        == "Player 1"
    assert output_payload[0].cost \
        == 100
    assert output_payload[1] \
        == 5
    assert basic_processor.output_payload is None
