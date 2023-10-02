"""
CS 5001
Spring 2023
Final Project - class VotingPlace
Hanyi(Hanna) Zhou

A class file of voting place.
"""

class VotingPlace:
    """Class representing a voting place with year, place name and place type name."""

    def __init__(self, year, place_name, type_name):
        """
        Initialize a VotingPlace object with the given year, place name and place type name.

        Parameters:
            year (str): The year of the voting place.
            place_name (str): The name of the voting place.
            type_name (str): The name of the voting place type.

        Raises:
            TypeError: If year or place_name or type_name is not a string.
            ValueError: If year or place_name or type_name is an empty string or only contains whitespace.
        """
        if not isinstance(year, str):
            raise TypeError("year must be a string.")
        if not isinstance(place_name, str):
            raise TypeError("place_name must be a string.")
        if not isinstance(type_name, str):
            raise TypeError("type_name must be a string.")
        if not year or year.isspace():
            raise ValueError("year is an empty string or contains whitespace.")
        if not place_name or place_name.isspace():
            raise ValueError("place_name is an empty string or contains whitespace.")
        if not type_name or type_name.isspace():
            raise ValueError("type_name is an empty string or contains whitespace.")

        self.year = year
        self.place_name = place_name
        self.type_name = type_name

    def __eq__(self, other):
        """
        Check whether two VotingPlace objects are equal.

        Parameters:
            other (object): The object to compare with.

        Returns:
            bool: True if the two VotingPlace objects are equal, False otherwise.
        """
        if isinstance(other, VotingPlace):
            if self.year == other.year and self.place_name == other.place_name and self.type_name == other.type_name:
                return True
        return False