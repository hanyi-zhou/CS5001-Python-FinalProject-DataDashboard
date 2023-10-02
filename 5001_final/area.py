"""
CS 5001
Spring 2023
Final Project - class Area
Hanyi(Hanna) Zhou

A class file of area.
"""

class Area():
    """Class representing an area with year, area name, and voting place type name."""

    def __init__(self, year, area, type_name):
        """
        Initialize an Area object with the given year, area name, and voting place type name.

        Parameters:
            year (str): The year of the area.
            area (str): The name of the area.
            type_name (str): The name of the voting place type in the area.

        Raises:
            TypeError: If year, area, or type_name is not a string.
            ValueError: If year, area, or type_name is an empty string or only contains whitespace.
        """
        if not isinstance(year, str):
            raise TypeError("year must be a string.")
        if not isinstance(area, str):
            raise TypeError("area must be a string.")
        if not isinstance(type_name, str):
            raise TypeError("type_name must be a string.")
        if not year or year.isspace():
            raise ValueError("year is an empty string or contains a whitespace.")
        if not area or area.isspace():
            raise ValueError("area is an empty string or contains a whitespace.")
        if not type_name or type_name.isspace():
            raise ValueError("type_name is an empty string or contains a whitespace.")

        self.year = year
        self.area = area
        self.type_name = type_name

    def __eq__(self, other):
        """
        Check whether two Area objects are equal.

        Parameters:
            other (object): The object to compare with.

        Returns:
            bool: True if the two Area objects are equal, False otherwise.
        """
        if isinstance(other, Area):
            if self.year == other.year and self.area == other.area and self.type_name == other.type_name:
                return True
        return False