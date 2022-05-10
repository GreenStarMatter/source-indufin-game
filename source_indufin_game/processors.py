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
            input_payload = [materials.MaterialUnit(), 0],
            ):
        """Inits the class with a mechanism, input_payload,
        and turns_to_produce"""

        self.mechanism = mechanism
        self.input_payload = input_payload
        if not self.verify_machine_can_handle_load(input_payload):
            self.input_payload = [materials.MaterialUnit(), 0]
            print("Improper payload, please set viable payload")
        self.turns_to_produce = self.mechanism.turns_to_process
        self.output_payload_ready_flag = 0
        self._processing_flag = 0
        self.output_payload = None
        self._define_output_payload()


    def __repr__(self):
        """The representation of the object so that it can be used as an
        abstract entity"""

        return f"ProcessorUnit({self.mechanism.__repr__()}, " +\
            f"{self.input_payload}, {self.turns_to_produce})"


    def __str__(self):
        """The representation of the object so that it can understood
        as a representation"""

        return f"The mechanism {self.mechanism.machine_name} will " +\
            f"process {self.input_payload[0].material_name} in " +\
            f"{self.turns_to_produce} turn(s)"

    def _allowable_combination(self, material_name, processable_inputs):
        """Detect if mechanism can accept input_payload"""

        return material_name in processable_inputs


    def _define_output_payload(self):
        """Define output payload by mechanism and input_payload"""

        self.output_payload_ready_flag = 0
        if (self.mechanism.machine_name == "Generic Machine" or\
                self.input_payload[0].material_name == 'Generic Material'):
            self.output_payload = None
        else:
            self.turns_to_produce = self.mechanism.turns_to_process
            self._processing_flag = 1
            self.output_payload = [materials.MaterialUnit(
                cost = self.input_payload[0].cost,
                owner = self.input_payload[0].owner,
                material_name = self.input_payload[0].material_name,
                form = self.mechanism.augment + "ed",
                form_potency = self.mechanism.augment_potency
                ),  self.input_payload[1]]



    def decrement_processor_tracker(self):
        """Decrements from the processor time if the processor is in a
        processing state.  If the processor is ready, then move the processor
        out of the processing state."""

        if self._processing_flag:
            self.turns_to_produce -= 1
            if self.turns_to_produce == 0:
                self.output_payload_ready_flag = 1
                self._processing_flag = 0

    def output_payload_ready(self):
        "Verify that output payload is ready for collection"

        return self.output_payload_ready_flag


    def collect_output_payload(self):
        """If output payload is ready for collection, pop output out of
        processor."""

        if self.output_payload_ready():
            output_to_return = self.output_payload
            self.output_payload = None
            self.output_payload_ready_flag = 0
            return output_to_return
        print("Output payload not ready")
        return None

    def _check_new_payload(self, new_payload):
        """Check if a new payload can be processed by mechansim"""
        return self._allowable_combination(new_payload[0].material_name,
                                     self.mechanism.processable_inputs)


    def _check_new_mechanism(self, new_mechanism):
        """Check if a new mechanism can be process material"""

        return self._allowable_combination(self.input_payload[0].material_name,
                                     new_mechanism.processable_inputs)


    def verify_payload_machine_viability_tests(self, new_payload):
        """Verify payload allowable."""

        payload_allowable = True
        if not self._check_new_payload(new_payload):
            print(f"Payload: {new_payload.material_name}")
            print(f"Nonviable payload, please select from{chr(10)}"+\
                  f"{chr(10).join(self.mechanism.processable_inputs)}")
            payload_allowable = False
        if not self.verify_machine_can_handle_load(new_payload):
            print(f"Payload: {new_payload[0].material_name}, {new_payload[1]}")
            print(f"Payload over machine capcity, {self.mechanism.capacity}"+\
                  f"{chr(10).join(self.mechanism.processable_inputs)}")
            payload_allowable = False
        return payload_allowable


    def set_payload(self, new_payload):
        """If payload is allowable, then input it to processor.
        Define the output payload as well."""
        if self.verify_payload_machine_viability_tests(new_payload):
            self.input_payload = new_payload
            self._define_output_payload()



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


    def verify_machine_can_handle_load(self, new_payload):
        """Verify machine capacity is greater than the input_load"""

        return new_payload[1] <= self.mechanism.capacity
