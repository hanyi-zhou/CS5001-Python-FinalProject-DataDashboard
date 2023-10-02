"""
CS 5001
Spring 2023
Final Project - type_number_and_ratio_analysis
Hanyi(Hanna) Zhou

A function file to analyze the number and ratio to the total changed of a voting place type input by the user for years 2014/2018/2022.
"""

from voting_place import VotingPlace

from constants import  SCHOOL_KEY_WORDS, COMMUNITY_CENTRE_KEY_WORDS, CHURCH_KEY_WORDS, SCHOOL, COMMUNITY_CENTRE, CHURCH, ELSE

# classify the type of a voting place based on its name
def classify_place_type(place_name):
    """
    Classifies the type of a voting place based on its name.

    Parameters:
        place_name (str): A string representing the name of the voting place.

    Returns:
        str: A string representing the type of the voting place. Possible values are 'School', 'Community Centre', 'Church', or 'Else'.

    Raises:
        TypeError: If place_name is not a string.
        ValueError: If place_name is an empty string or only contains whitespace.
    """
    if not isinstance(place_name, str):
        raise TypeError("place_name must be a string.")
    if not place_name or place_name.isspace():
        raise ValueError("place_name is an empty string or contains a whitespace.")
    for word in place_name.split():
        if word in SCHOOL_KEY_WORDS:
            return SCHOOL
        elif word in COMMUNITY_CENTRE_KEY_WORDS:
            return COMMUNITY_CENTRE
        elif word in CHURCH_KEY_WORDS:
            return CHURCH
    return ELSE

# create a list of VotingPlace objects
def create_place_objects_list(year, place_names):
    """
    Creates a list of VotingPlace objects for a given year and list of place names.

    Parameters:
        year (str): The year for which the VotingPlace objects are created.
        place_names (list): A list of place names for which VotingPlace objects are created.

    Returns:
        place_objects (list): A list of VotingPlace objects created for the given year and list of place names.

    Raises:
        TypeError: If year is not a string or place_names is not a list.
        ValueError: If place_names is empty.
    """
    if not isinstance(year, str):
        raise TypeError("year must be a string.")
    if not isinstance(place_names, list):
        raise TypeError("place_names must be a list.")
    if not place_names:
        raise ValueError("place_names is empty.")
    place_objects = []
    for place_name in place_names:
        type_name = classify_place_type(place_name)
        place_object = VotingPlace(year, place_name, type_name)
        place_objects.append(place_object)
    return place_objects

# count the number of voting places of a type input by the user in a VotingPlace objects list
def count_type(place_objects, input_type):
    """
    Counts the number of voting places of a type input by the user in a VotingPlace objects list.

    Parameters:
        place_objects (list): A list of VotingPlace objects.
        input_type (str): A string representing the type of the voting place input by the user.

    Returns:
        type_count (int): An integer representing the number of voting places of the input type.

    Raises:
        TypeError: If place_objects is not a list, or input_type is not a string.
        ValueError: If place_objects is an empty list.
    """
    if not isinstance(place_objects, list):
        raise TypeError("place_objects must be a list.")
    if not isinstance(input_type, str):
        raise TypeError("input_type must be a string.")
    if not place_objects:
        raise ValueError("place_objects cannot be empty.")
    type_count = 0
    for place_object in place_objects:
        if place_object.type_name.lower() == input_type.lower():
            type_count += 1
    return type_count

# calculate the ratio of the number a type to the total number of voting places
def calculate_type_ratio(place_objects, type_count):
    """
    Calculates the ratio of the number of voting places of a specific type to the total number of voting places.

    Parameters:
        place_objects (list): A list of VotingPlace objects.
        type_count (int): The number of voting places of the type being calculated.

    Returns:
        type_ratio(str): A string representing the ratio of the number of voting places of the specific type to the total number of voting places.

    Raises:
        TypeError: If place_objects is not a list or type_count is not an integer.
        ValueError: If place_objects is empty, or type_count is greater than the length of place_objects.
    """
    if not isinstance(place_objects, list):
        raise TypeError("place_objects must be a list.")
    if not isinstance(type_count, int):
        raise TypeError("type_count must be an integer.")
    if not place_objects:
        raise ValueError("place_objects cannot be empty.")
    if type_count > len(place_objects):
        raise ValueError("type_count is greater than the length of place_objects.")
    type_ratio = type_count / len(place_objects)
    return '{:.2%}'.format(type_ratio)