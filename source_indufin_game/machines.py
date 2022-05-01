# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:26:11 2022

@author: Kyle Stanley
"""

class MachineUnit():
    """This class is intended to hold all possible things a machine can do.
    Currently, machines are single function though they may take in many
    inputs.  They can be owned and named.  Each machine will have an
    associated cost, shape, and size.  The size will be determined from the
    shape.  The shape will interact with a grid which is not yet implemented.
    This will likely be updated once more information is known about the grid
    implementation.

    cost: Cost of the machine.
    shape: Grid shape that the machine occupies
    owner: Name of the machine owner
    machine_name: Name of the machine
    processable_inputs: The inputs that a machine can intake
    augment: The way which inputs will be changed
    augment_potency: The max potency of which the inputs will be augmented
    """

    def __init__(
            self,
            cost = 0,
            shape = [1],
            owner = "None Assigned",
            machine_name = "Generic Machine",
            processable_inputs = ["None"],
            augment = "No Augmentation",
            augment_potency = 0
            ):
        """Inits the class with a cost, shape, owner, machine name,
        processable_inputs, augment, and augment_potency"""

        self.cost = cost
        self.size = sum(shape)
        self.shape = shape
        self.owner = owner
        self.machine_name = machine_name
        self.processable_inputs = set(processable_inputs)
        self.augment = augment
        self.augment_potency = augment_potency

    def __repr__(self):
        """The representation of the object so that it can be used as an
        abstract entity"""

        return f"MachineUnit({self.cost}, {self.shape}, " + \
            "{self.owner}, {self.machine_name}, " + \
            "{self.processable_inputs}, {self.augment}, " + \
            "{self.augment_potency})"

    def __str__(self):
        """The representation of the object so that it can understood
        as a representation"""

        return f"The machine {self.machine_name} of {self.owner}" +\
            f" has been a cost of: {self.cost:,}. \n" +\
            f"It can {self.augment} {self.augment_potency} the " +\
            "following inputs: " +\
            f"{chr(10)}{chr(10).join(self.processable_inputs)}" +\
            "It has a shape: \n" +\
            f"{chr(10)}{chr(10).join(self.shape)}"


    def set_cost(self, new_cost):
        """Allows the ability to manually set the cost amount"""

        self.cost = new_cost


    def set_owner(self, new_owner):
        """Allows the ability to manually set the machine owner"""

        self.owner = new_owner


    def set_shape(self, new_shape):
        """Allows the ability to manually set the machine shape"""

        self.shape = new_shape
        self.size = sum(self.shape)


    def set_machine_name(self, new_machine_name):
        """Allows the ability to manually set the machine name"""

        self.machine_name = new_machine_name


    def set_processable_inputs(self, new_processable_inputs):
        """Allows the ability to manually set the inputs which the machine
        can process"""

        self.processable_inputs = set(new_processable_inputs)


    def set_augment(self, new_augment):
        """Allows the ability to manually set how the materials which the
        machine process are augmented"""

        self.augment = new_augment


    def set_augment_potency(self, new_augment_potency):
        """Allows the ability to manually set the degree to which the materials
        the machine process are augmented"""

        self.augment_potency = new_augment_potency


    def add_processable_input(self, new_processable_inputs):
        """Allows the ability to add an item to the processable inputs"""

        self.processable_inputs.add(new_processable_inputs)

    def remove_processable_input(self, remove_processable_inputs):
        """Allows the ability to add an item to the processable inputs"""

        if remove_processable_inputs in self.processable_inputs:
            self.processable_inputs.add(remove_processable_inputs)
        else:
            print(f"{remove_processable_inputs} already not allowable")
