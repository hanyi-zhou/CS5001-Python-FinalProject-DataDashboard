"""
CS 5001
Spring 2023
Final Project - test_get_user_input
Hanyi(Hanna) Zhou

A file to test get_user_input functions.
"""
import unittest
from get_user_input import get_area_input, create_areas_name_list

# test get_area_input
class TestGetAreaInput(unittest.TestCase):

    def test_empty_list(self):
        areas = []
        with self.assertRaises(ValueError):
            get_area_input(areas)

    def test_non_list_input(self):
        areas = "Downtown, Strathcona"
        with self.assertRaises(TypeError):
            get_area_input(areas)

# test create_areas_name_list
class TestCreateAreasNameList(unittest.TestCase):

    def test_valid_input(self):
        areas_year1 = ["Downtown", "Strathcona"]
        areas_year2 = ["Strathcona", "Fairview"]
        areas_year3 = ["Fairview", "Sunset"]
        expected = ["downtown", "fairview", "strathcona", "sunset"]
        result = create_areas_name_list(areas_year1, areas_year2, areas_year3)
        self.assertEqual(result, expected)

    def test_empty_list_input(self):
        areas_year1 = []
        areas_year2 = ["Strathcona", "Fairview"]
        areas_year3 = ["Fairview", "Sunset"]
        with self.assertRaises(ValueError):
            create_areas_name_list(areas_year1, areas_year2, areas_year3)

    def test_non_list_input(self):
        areas_year1 = "Downtown, Strathcona"
        areas_year2 = ["Strathcona", "Fairview"]
        areas_year3 = ["Fairview", "Sunset"]
        with self.assertRaises(TypeError):
            create_areas_name_list(areas_year1, areas_year2, areas_year3)

def main():
    """
    Ran 5 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()