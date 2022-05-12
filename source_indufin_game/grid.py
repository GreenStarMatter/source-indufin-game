# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:27:42 2022

@author: Kyle Stanley
"""

from collections import defaultdict

class FactoryGrid():
    """This class represents the playable field which machines can be put on.
    It will store the objects placed on it in a defaultdict.  Objects can be
    removed by a public method."""
    def __init__(self, shape = (0,0)):
        self.set_grid_attributes(shape)
        self.objects_on_grid = defaultdict(tuple)


    def set_grid_attributes(self, new_shape):
        """Quick set to grid attributes.  Most of grid attributes are
        dependent on the shape."""

        self.shape = new_shape
        self.x = new_shape[0]
        self.y = new_shape[1]
        self.grid = [["O"]*self.x for line in range(self.y)]


    def __repr__(self):
        """Functional representation of FactoryGrid"""

        return f"FactoryGrid({self.shape})"


    def __str__(self):
        """Pretty grid output.  Print this to get a more readable grid."""

        top_base_border = "-"*(self.x*2 + 1)
        middle_lines = "\n".join(["|"+" ".join(O)+ "|" for O in self.grid])
        return "\n".join([top_base_border, middle_lines, top_base_border])


    def get_shape_coordinates(self, object_to_place, pin_coordinates):
        """Maps the coordinates of the object to place in terms of the grid
        space it will occupy... may be better implemented using map functions.
        However, this is a fairly straightforward implementation and is
        readable."""

        board_coordinate_pairs = []
        for coord_y,row in enumerate(object_to_place.shape):
            for coord_x in range(len(row)):
                board_coordinate_pairs.append([coord_x + pin_coordinates[0],
                                               coord_y + pin_coordinates[1]])
        return board_coordinate_pairs


    def place_on_grid(self, object_to_place, coordinates):
        """Place item on grid.  Placement coordinate is always top left most
        index of object.  This looks nasty right now.  Definitely is a cleaner
        way to write this.  Nested, direct index using... not even syntatic
        sugar to make it difficult to read."""
        if self.verify_valid_placement(object_to_place, coordinates):
            placement_targets = self.get_shape_coordinates(object_to_place,
                                                           coordinates)
            for place_coord in placement_targets:
                self.grid[place_coord[1]][place_coord[0]] = "X"

            self.objects_on_grid[object_to_place] = coordinates
        else:
            print("Invalid placement of object")
            print("Grid remains the same")


    def verify_valid_placement(self, object_to_place, coordinates):
        """Valid placement first checks if object is within grid.  This is
        done before checking if the grid spaces are unused to avoid outside of
        index errors."""

        valid_place = False
        if self.check_inside_grid(object_to_place, coordinates):
            if self.check_grid_space_unused(object_to_place, coordinates):
                valid_place =  True
        return valid_place

    def check_inside_grid(self, object_to_place, coordinates):
        """Verify that object will not overflow out of grid."""

        x_right_bound = len(object_to_place.shape[0]) + coordinates[0]
        y_bottom_bound = len(object_to_place.shape) + coordinates[1]
        x_in_bounds = (coordinates[0] >= 0)  and (x_right_bound <= self.x)
        y_in_bounds = (coordinates[1] >= 0)  and (y_bottom_bound <= self.y)

        return x_in_bounds and y_in_bounds


    def check_grid_space_unused(self, object_to_place, coordinates):
        """Verify that grid spaces are unused where object will be placed."""
        collision_detected = False

        y_dist = len(object_to_place.shape)
        for row in range(coordinates[1], coordinates[1] + y_dist):
            collision_detected = collision_detected or\
                any(check_coord != "O" for check_coord in\
                    self.grid[row][coordinates[0] : coordinates[0] +\
                                   len(object_to_place.\
                                       shape[coordinates[1] - row])])
        return not collision_detected


    def remove_from_grid(self, object_to_remove):
        """Removes object on grid from grid.  Also removes object from list of
        contained object on grid."""
        if object_to_remove in self.objects_on_grid:
            coordinates = self.objects_on_grid[object_to_remove]
            placement_targets = self.get_shape_coordinates(object_to_remove,
                                               coordinates)
            for place_coord in placement_targets:
                self.grid[place_coord[1]][place_coord[0]] = "O"
            del self.objects_on_grid[object_to_remove]
        else:
            print(f"Machine not in grid: \n{self.objects_on_grid}")
