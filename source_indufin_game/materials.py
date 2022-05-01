# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:24:28 2022

@author: Kyle Stanley
"""


class MaterialUnit():
    """This class is intended to hold all possible things a material is.

    cost: Cost of a unit of material.
    owner: Name of the material owner
    material_name: Name of the material
    form: The way which inputs the material is formed/augmented
    form_potency: The potency of which the material is formed/augmented
    """

    def __init__(
            self,
            cost = 0,
            owner = "None Assigned",
            material_name = "Generic Material",
            form = "Raw",
            form_potency = 0
            ):
        """Inits the class with a cost, owner, material_name, form,
        and form_potency"""

        self.cost = cost
        self.owner = owner
        self.material_name = material_name
        self.form = form
        self.form_potency = form_potency

    def __repr__(self):
        """The representation of the object so that it can be used as an
        abstract entity"""

        return f"MaterialUnit({self.cost}, {self.owner}, " + \
            f"{self.material_name}, {self.form}, {self.form_potency})"

    def __str__(self):
        """The representation of the object so that it can understood
        as a representation"""

        return f"The level {self.form_potency} {self.form} " +\
            f"{self.material_name} belonging to {self.owner} has a unit " +\
            f"cost of: {self.cost:,}"


    def set_cost(self, new_cost):
        """Allows the ability to manually set the cost amount"""

        self.cost = new_cost


    def set_owner(self, new_owner):
        """Allows the ability to manually set the owner"""

        self.owner = new_owner


    def set_material_name(self, new_material_name):
        """Allows the ability to manually set the material name"""

        self.material_name = new_material_name


    def set_form(self, new_form):
        """Allows the ability to manually set how the material form"""

        self.form = new_form


    def set_form_potency(self, new_form_potency):
        """Allows the ability to manually set the degree to which the materials
        augmented"""

        self.form_potency = new_form_potency
