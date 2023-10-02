"""
CS 5001
Spring 2023
Final Project - area_type_number_analysis
Hanyi(Hanna) Zhou

A function file to analyze the number changed of 4 place types in an area input by the user for years 2014/2018/2022.
"""

from area import Area
from type_number_and_ratio_analysis import classify_place_type

from constants import SCHOOL, COMMUNITY_CENTRE, CHURCH, ELSE

# create a list of Area objects
def create_area_objects_list(year, areas, place_names):
    """
    Creates a list of Area objects.

    Parameters:
        year (str): The year of the area data.
        areas (list): A list of strings representing area names.
        place_names (list): A list of strings representing place names.

    Returns:
        area_objects (list): A list of Area objects.

    Raises:
        TypeError: If year is not an integer, or if areas or place_names is not a list.
        ValueError: If areas or place_names is empty, or they have different lengths.
    """
    if not isinstance(year, str):
        raise TypeError("year must be a string.")
    if not isinstance(areas, list):
        raise TypeError("areas must be a list.")
    if not isinstance(place_names, list):
        raise TypeError("place_names must be a list.")
    if not areas:
        raise ValueError("areas cannot be empty.")
    if not place_names:
        raise ValueError("place_names cannot be empty.")
    if len(areas) != len(place_names):
        raise ValueError("areas and place_names must have the same length.")
    area_objects = []
    for i in range(len(areas)):
        type_name = classify_place_type(place_names[i])
        area_object = Area(year, areas[i], type_name)
        area_objects.append(area_object)
    return area_objects

# count the number of each type in the given area
def count_type_in_area(area_objects, input_area):
    """
    Counts the number of each place type in a given area.

    Parameters:
        area_objects (list): A list of Area objects representing different areas.
        input_area (str): A string representing the area for which type counts need to be calculated.

    Returns:
        type_counts_in_area (list): A list of integers representing the counts of different place types in the given area.

    Raises:
        TypeError: If area_objects is not a list or input_area is not a string.
        ValueError: If area_objects is an empty list.
    """
    if not isinstance(area_objects, list):
        raise TypeError("area_objects must be a list.")
    if not isinstance(input_area, str):
        raise TypeError("input_area must be a string.")
    if not area_objects:
        raise ValueError("area_objects cannot be empty.")
    school_count_in_area = 0
    community_centre_count_in_area = 0
    church_count_in_area = 0
    else_count_in_area = 0
    for area_object in area_objects:
        if area_object.area.lower() == input_area.lower():
            if area_object.type_name == SCHOOL:
                school_count_in_area += 1
            elif area_object.type_name == COMMUNITY_CENTRE:
                community_centre_count_in_area += 1
            elif area_object.type_name == CHURCH:
                church_count_in_area += 1
            elif area_object.type_name == ELSE:
                else_count_in_area += 1
    type_counts_in_area = [school_count_in_area, community_centre_count_in_area, church_count_in_area, else_count_in_area]
    return type_counts_in_area