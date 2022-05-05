# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:27:44 2022

@author: Kyle Stanley
"""

from source_indufin_game import grid
from source_indufin_game import machines

def test_grid_creation():
    """Create a simple grid object"""

    player_grid = grid.FactoryGrid()
    assert player_grid.x == 0
    assert player_grid.y == 0
    assert player_grid.grid == []


def test_grid_set():
    """Create a grid with custom inputs"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    assert player_grid.x == 2
    assert player_grid.y == 3
    assert player_grid.grid == [["O", "O"],
                                ["O", "O"],
                                ["O", "O"]]

def test_valid_grid_placement():
    """Test a valid grid placement"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    player_grid.grid = [["O", "O"],
                        ["O", "X"],
                        ["O", "O"]]
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1],[1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)

    assert player_grid.check_inside_grid(basic_machine, (0,0))
    assert player_grid.check_grid_space_unused(basic_machine, (0,0))

def test_invalid_grid_placement_wall_and_collision():
    """Test two invalid grid placement: wall collision and object collision"""
    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    player_grid.grid = [["O", "O"],
                        ["X", "X"],
                        ["O", "O"]]
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1],[1],[1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)

    assert not player_grid.check_inside_grid(basic_machine, (0,2))
    assert not player_grid.check_grid_space_unused(basic_machine, (0,0))

def test_place_on_grid_valid():
    """Test a valid grid placement change to the grid"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    assert player_grid.x == 2
    assert player_grid.y == 3
    assert player_grid.grid == [["O", "O"],
                                ["O", "O"],
                                ["O", "O"]]
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1,1],[1,1],[1,1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)
    player_grid.place_on_grid(basic_machine, (0,0))

    assert player_grid.grid == [["X", "X"],
                                ["X", "X"],
                                ["X", "X"]]

def test_place_on_grid_invalid():
    """Test an invalid grid placement change to the grid"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1,1,1],[1,1,1],[1,1,1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)
    player_grid.place_on_grid(basic_machine, (0,0))

    assert player_grid.grid == [["O", "O"],
                                ["O", "O"],
                                ["O", "O"]]

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((2,3))
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1],[1],[1],[1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)
    player_grid.place_on_grid(basic_machine, (0,0))

    assert player_grid.grid == [["O", "O"],
                                ["O", "O"],
                                ["O", "O"]]

def test_remove_from_grid_valid():
    """Test a valid removal of an object from the grid"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((3,4))
    assert player_grid.x == 3
    assert player_grid.y == 4
    assert player_grid.grid == [["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"]]
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1,1],[1,1],[1,1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)
    player_grid.place_on_grid(basic_machine, (0,0))

    assert player_grid.grid == [["X", "X", "O"],
                                ["X", "X", "O"],
                                ["X", "X", "O"],
                                ["O", "O", "O"]]

    player_grid.remove_from_grid(basic_machine)
    assert player_grid.grid == [["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"]]
    assert not any(player_grid.objects_on_grid)

def test_remove_from_grid_no_machines():
    """Test an invalid removal of an object from the grid"""

    player_grid = grid.FactoryGrid()
    player_grid.set_grid_attributes((3,4))
    assert player_grid.x == 3
    assert player_grid.y == 4
    assert player_grid.grid == [["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"]]
    basic_machine = machines.MachineUnit(
        cost = 100,
        shape = [[1,1],[1,1],[1,1]],
        owner = "Player 1",
        machine_name = "Testulator",
        processable_inputs = ["Testonium", "Testadon"],
        augment = "Melt",
        augment_potency = 3)

    player_grid.remove_from_grid(basic_machine)
    assert player_grid.grid == [["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"],
                                ["O", "O", "O"]]
