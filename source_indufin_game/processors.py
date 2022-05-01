# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:02:38 2022

@author: Kyle Stanley
"""

from source_indufin_game import machines
from source_indufin_game import materials


class ProcessorUnit():
    """This class is intended to hold all possible things a processor is.

    mechanism: Unit which will hold an input payload for processing.
    input_payload: Input which will be processed
    turns_to_produce: Amount of time until input will be processed.
    """

    def __init__(
            self,
            mechanism = machines.MachineUnit(),
            input_payload = materials.MaterialUnit(),
            turns_to_produce = 0
            ):
        """Inits the class with a mechanism, input_payload,
        and turns_to_produce"""

        self.mechanism = mechanism
        self.input_payload = input_payload
        self.turns_to_produce = turns_to_produce
        self._define_output_payload()


    def __repr__(self):
        """The representation of the object so that it can be used as an
        abstract entity"""

        return f"ProcessorUnit({self.mechanism}, {self.input_payload}, " + \
            f"{self.turns_to_produce}"


    def __str__(self):
        """The representation of the object so that it can understood
        as a representation"""

        return f"The mechanism {self.mechanism.machine_name} will " +\
            f"process {self.input_payload.material_name} in " +\
            f"{self.turns_to_produce}"

    def _allowable_combination(self, material_name, processable_inputs):
        """Detect if mechanism can accept input_payload"""

        return material_name in processable_inputs


    def _define_output_payload(self):
        """Define output payload by mechanism and input_payload"""

        if not (self.mechanism and self.input_payload):
            self.output_payload = None
        else:
            self.output_payload = materials.MaterialUnit(
                cost = self.input_payload.cost,
                owner = self.input_payload.owner,
                material_name = self.input_payload.material_name,
                form = self.mechanism.augment + "ed",
                form_potency = self.mechanism.augment_potency
                )


    def _check_new_payload(self, new_payload):
        """Check if a new payload can be processed by mechansim"""

        return self._allowable_combination(new_payload.material_name,
                                     self.mechanism.processable_inputs)


    def _check_new_mechanism(self, new_mechanism):
        """Check if a new mechanism can be process material"""

        return self._allowable_combination(self.input_payload.material_name,
                                     new_mechanism.processable_inputs)


    def set_payload(self, new_payload):
        """If payload is allowable, then input it to processor.
        Define the output payload as well."""

        if self._check_new_payload(new_payload):
            self.input_payload = new_payload
            self._define_output_payload()
        else:
            print(f"Payload: {new_payload.material_name}")
            print(f"Nonviable payload, please select from{chr(10)}"+\
                  f"{chr(10).join(self.mechanism.processable_inputs)}")


    def set_mechanism(self, new_mechanism):
        """If mechanism is allowable, then input it to processor.
        Define the output payload as well."""

        if self._check_new_mechanism(new_mechanism):
            self.mechanism = new_mechanism
            self._define_output_payload()
        else:
            print(f"Mechanism: {self.mechanism.machine_name}")
            print(f"Nonviable mechanism, material not in from{chr(10)}"+\
                  f"{chr(10).join(self.mechanism.processable_inputs)}")
