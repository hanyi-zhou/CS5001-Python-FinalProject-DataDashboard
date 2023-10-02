"""
CS 5001
Spring 2023
Final Project - test_area
Hanyi(Hanna) Zhou

A file to test Area class.
"""

import unittest

from area import Area
from voting_place import VotingPlace

# test Area class
class TestArea(unittest.TestCase):

    def test_init_valid_input(self):
        area = Area("2022", "Downtown", "Community Centre")
        self.assertEqual(area.year, "2022")
        self.assertEqual(area.area, "Downtown")
        self.assertEqual(area.type_name, "Community Centre")

    def test_init_invalid_year(self):
        with self.assertRaises(ValueError):
            Area("", "Downtown", "Community Centre")
        with self.assertRaises(ValueError):
            Area("  ", "Downtown", "Community Centre")
        with self.assertRaises(TypeError):
            Area(2022, "Downtown", "Community Centre")

    def test_init_invalid_area(self):
        with self.assertRaises(ValueError):
            Area("2022", "", "Community Centre")
        with self.assertRaises(ValueError):
            Area("2022", "  ", "Community Centre")
        with self.assertRaises(TypeError):
            Area("2022", ["Downtown"], "Community Centre")

    def test_init_invalid_type_name(self):
        with self.assertRaises(ValueError):
            Area("2022", "Downtown", "")
        with self.assertRaises(ValueError):
            Area("2022", "Downtown", "  ")
        with self.assertRaises(TypeError):
            Area("2022", "Downtown", ["Community Centre"])

    def test_eq(self):
        a1 = Area("2022", "Downtown", "Community Centre")
        a2 = Area("2022", "Downtown", "Community Centre")
        a3 = Area("2022", "West End", "Community Centre")
        a4 = Area("2018", "Downtown", "Community Centre")
        vp = VotingPlace("2022", "Vancouver City Hall", "Else")
        self.assertTrue(a1 == a2)
        self.assertFalse(a1 == a3)
        self.assertFalse(a1 == a4)
        self.assertFalse(a1 == vp)

def main():
    """
    Ran 5 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()