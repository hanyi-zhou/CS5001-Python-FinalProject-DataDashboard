"""
CS 5001
Spring 2023
Final Project - get_user_input
Hanyi(Hanna) Zhou

A function file to get a valid type name or area name from the user input.
"""

from constants import VALID_TYPE_INPUT

# get a valid type_input from the user
def get_type_input():
    """
    Gets a valid voting place type from user input.

    Returns:
        input_type (str): A valid voting place type selected by the user.
    """
    valid_type = 0
    while valid_type == 0:
        input_type = input("Please input a voting place type(School/Community Centre/Church/Else):")
        if input_type.lower() not in VALID_TYPE_INPUT:
            print("Invalid input. Please input a voting place type again (School/Community Centre/Church/Else).")
        else:
            valid_type = 1
    return input_type

# get a valid area_input from the user
def get_area_input(areas_name_list):
    """
    Gets a valid area name from the user, given a set of valid area names.

    Parameters:
        areas_name_list (list): A list of strings representing valid area names.

    Returns:
        input_area(str): A string representing a valid area name input by the user.

    Raises:
        TypeError: If areas_name_list is not a list.
        ValueError: If areas_name_list is an empty set.
    """
    if not isinstance(areas_name_list, list):
        raise TypeError("areas_name_list must be a list.")
    if not areas_name_list:
        raise ValueError("areas_name_list cannot be an empty list.")
    valid_area = 0
    while valid_area == 0:
        for area_name in areas_name_list:
            print(area_name)
        input_area = input("Please input an area name from the above name list:")
        if input_area.lower() not in areas_name_list:
            print("Invalid input. You may choose one valid name from the name list, please input again.")
        else:
            valid_area = 1
    return input_area

# creates a list of unique area names form the three years
def create_areas_name_list(areas_year1, areas_year2, areas_year3):
    """
    Creates a list of unique area names of lowercase in alphabetical order given three lists of area names.

    Parameters:
        areas_year1 (list): A list of strings representing area names for year 1.
        areas_year2 (list): A list of strings representing area names for year 2.
        areas_year3 (list): A list of strings representing area names for year 3.

    Returns:
        areas_name_list (list): A list of strings representing unique area names from all three lists.

    Raises:
        TypeError: If any of the arguments is not a list.
        ValueError: If any of the arguments is an empty list.
    """
    if not isinstance(areas_year1, list) or not isinstance(areas_year2, list) or not isinstance(areas_year3, list):
        raise TypeError("All arguments must be lists.")
    if not areas_year1 or not areas_year2 or not areas_year3:
        raise ValueError("All arguments cannot be empty lists.")
    areas_set = set(areas_year1 + areas_year2 + areas_year3)
    areas_name_list = sorted([area.lower() for area in areas_set])
    return areas_name_list