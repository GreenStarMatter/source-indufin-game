# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:24:45 2022

@author: Kyle Stanley

This test the material logic.  This will test the attributes of each
material and the ability to change these attributes.
"""

from source_indufin_game import materials


def test_material_object_shape():
    """Tests basics of account creation"""

    basic_material = materials.MaterialUnit()
    assert basic_material
    assert basic_material.cost == 0
    assert basic_material.owner == "None Assigned"
    assert basic_material.material_name == "Generic Material"
    assert basic_material.form == "Raw"
    assert basic_material.form_potency == 0

    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Melted",
        form_potency = 3)
    assert basic_material.cost == 100
    assert basic_material.owner == "Player 1"
    assert basic_material.material_name == "Testonium"
    assert basic_material.form == "Melted"
    assert basic_material.form_potency == 3


def test_material_altering_shape():
    """Tests basics of account creation"""

    basic_material = materials.MaterialUnit(
        cost = 100,
        owner = "Player 1",
        material_name = "Testonium",
        form = "Melted",
        form_potency = 3)

    basic_material.set_cost(10)
    basic_material.set_owner("Player 2")
    basic_material.set_material_name("Retestulator")
    basic_material.set_form("Strengthened")
    basic_material.set_form_potency(5)

    assert basic_material.cost == 10
    assert basic_material.owner == "Player 2"
    assert basic_material.material_name == "Retestulator"
    assert basic_material.form == "Strengthened"
    assert basic_material.form_potency == 5
