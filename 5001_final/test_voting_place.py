"""
CS 5001
Spring 2023
Final Project - test_voting_place
Hanyi(Hanna) Zhou

A file to test VotingPlace class.
"""

import unittest

from  voting_place import VotingPlace
from area import Area

# test VotingPlace class
class TestVotingPlace(unittest.TestCase):

    def test_init_valid_input(self):
        place = VotingPlace("2022", "Carnegie Centre", "Community Centre")
        self.assertEqual(place.year, "2022")
        self.assertEqual(place.place_name, "Carnegie Centre")
        self.assertEqual(place.type_name, "Community Centre")

    def test_init_invalid_year(self):
        with self.assertRaises(ValueError):
            VotingPlace("", "Carnegie Centre", "Community Centre")
        with self.assertRaises(ValueError):
            VotingPlace("  ", "Carnegie Centre", "Community Centre")
        with self.assertRaises(TypeError):
            VotingPlace(2022, "Carnegie Centre", "Community Centre")

    def test_init_invalid_place_name(self):
        with self.assertRaises(ValueError):
            VotingPlace("2022", "", "Community Centre")
        with self.assertRaises(ValueError):
            VotingPlace("2022", "  ", "Community Centre")
        with self.assertRaises(TypeError):
            VotingPlace("2022", ["Carnegie Centre"], "Community Centre")

    def test_init_invalid_type_name(self):
        with self.assertRaises(ValueError):
            VotingPlace("2022", "Carnegie Centre", "")
        with self.assertRaises(ValueError):
            VotingPlace("2022", "Carnegie Centre", "  ")
        with self.assertRaises(TypeError):
            VotingPlace("2022", "Carnegie Centre", ["Community Centre"])

    def test_eq(self):
        vp1 = VotingPlace("2022", "Queen Victoria Annex", "School")
        vp2 = VotingPlace("2022", "Queen Victoria Annex", "School")
        vp3 = VotingPlace("2022", "Broadway Church", "Church")
        vp4 = VotingPlace("2018", "Vancouver Public Library Central Branch", "Else")
        ar = Area("2022", "Downtown", "Community Centre")
        self.assertTrue(vp1 == vp2)
        self.assertFalse(vp1 == vp3)
        self.assertFalse(vp1 == vp4)
        self.assertFalse(vp1 == ar)

def main():
    """
    Ran 5 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()