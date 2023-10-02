"""
CS 5001
Spring 2023
Final Project - test_analysis_functions
Hanyi(Hanna) Zhou

A file to test analysis functions.
"""

import unittest

from voting_place import VotingPlace
from area import Area
from type_number_and_ratio_analysis import classify_place_type, create_place_objects_list, count_type, calculate_type_ratio
from area_type_number_analysis import create_area_objects_list, count_type_in_area

# test classify_place_type
class TestClassifyPlaceType(unittest.TestCase):

    def test_valid_place_name_school(self):
        place_name = "Gladstone Secondary School"
        expected_result = "School"
        self.assertEqual(classify_place_type(place_name), expected_result)

    def test_valid_place_name_community_centre(self):
        place_name = "Culloden Court Community Hall"
        expected_result = "Community Centre"
        self.assertEqual(classify_place_type(place_name), expected_result)

    def test_valid_place_name_church(self):
        place_name = "Broadway Church"
        expected_result = "Church"
        self.assertEqual(classify_place_type(place_name), expected_result)

    def test_valid_place_name_else(self):
        place_name = "Vancouver Public Library Central Branch"
        expected_result = "Else"
        self.assertEqual(classify_place_type(place_name), expected_result)

    def test_empty_place_name(self):
        place_name = ""
        with self.assertRaises(ValueError):
            classify_place_type(place_name)

    def test_only_whitespace_place_name(self):
        place_name = "    "
        with self.assertRaises(ValueError):
            classify_place_type(place_name)

    def test_invalid_place_name(self):
        place_name = 123
        with self.assertRaises(TypeError):
            classify_place_type(place_name)

# test create_place_objects_list
class TestCreatePlaceObjectsList(unittest.TestCase):

    def test_valid_input(self):
        year = "2022"
        place_names = ["High School", "Community Center", "Church"]
        expected_output = [
            VotingPlace("2022", "High School", "School"),
            VotingPlace("2022", "Community Center", "Community Centre"),
            VotingPlace("2022", "Church", "Church")
        ]
        self.assertEqual(create_place_objects_list(year, place_names), expected_output)

    def test_invalid_year(self):
        year = 2022
        place_names = ["Queen Victoria Annex", "Hillcrest Centre", "Trinity Baptist Church", "Vancouver City Hall"]
        with self.assertRaises(TypeError):
            create_place_objects_list(year, place_names)

    def test_invalid_place_names(self):
        year = "2022"
        place_names = "Queen Victoria Annex, Hillcrest Centre, Trinity Baptist Church, Vancouver City Hall"
        with self.assertRaises(TypeError):
            create_place_objects_list(year, place_names)

    def test_empty_place_names(self):
        year = "2022"
        place_names = []
        with self.assertRaises(ValueError):
            create_place_objects_list(year, place_names)

    def test_place_names_contain_whitespace_only(self):
        year = "2022"
        place_names = ["   ", " ", "  ", " "]
        with self.assertRaises(ValueError):
            create_place_objects_list(year, place_names)

# test count_type
class TestCountType(unittest.TestCase):

    place_objects = [
        VotingPlace('2022', 'Hillcrest Centre', 'Community Center'),
        VotingPlace('2022', 'Chief Maquinna Elementary School', 'School'),
        VotingPlace('2022', 'Killarney Community Centre', 'Community Center'),
        VotingPlace('2022', 'Redemption Church', 'Church'),
        VotingPlace('2022', 'Vancouver City Hall', 'Else')
    ]

    def test_count_type_valid(self):
        self.assertEqual(count_type(self.place_objects, 'Community Center'), 2)
        self.assertEqual(count_type(self.place_objects, 'School'), 1)
        self.assertEqual(count_type(self.place_objects, 'Church'), 1)
        self.assertEqual(count_type(self.place_objects, 'Else'), 1)

    def test_count_type_invalid(self):
        with self.assertRaises(TypeError):
            count_type(self.place_objects, 123)
        with self.assertRaises(TypeError):
            count_type(123, 'School')
        with self.assertRaises(ValueError):
            count_type([], 'School')

# test calculate_type_ratio
class TestCalculateTypeRatio(unittest.TestCase):

    place_objects = [
        VotingPlace('2022', 'Hillcrest Centre', 'Community Center'),
        VotingPlace('2022', 'Chief Maquinna Elementary School', 'School'),
        VotingPlace('2022', 'Killarney Community Centre', 'Community Center'),
        VotingPlace('2022', 'Redemption Church', 'Church'),
        VotingPlace('2022', 'Vancouver City Hall', 'Else')
    ]

    def test_calculate_type_ratio_valid(self):
        self.assertEqual(calculate_type_ratio(self.place_objects, 3), '60.00%')
        self.assertEqual(calculate_type_ratio(self.place_objects, 2), '40.00%')
        self.assertEqual(calculate_type_ratio(self.place_objects, 1), '20.00%')
        self.assertEqual(calculate_type_ratio(self.place_objects, 0), '0.00%')

    def test_calculate_type_ratio_invalid(self):
        with self.assertRaises(TypeError):
            calculate_type_ratio(self.place_objects, "not an integer")
        with self.assertRaises(TypeError):
            calculate_type_ratio("not a list", 2)
        with self.assertRaises(ValueError):
            calculate_type_ratio([], 2)
        with self.assertRaises(ValueError):
            calculate_type_ratio(self.place_objects, 6)

# test create_area_objects_list
class TestCreateAreaObjectsList(unittest.TestCase):

    year = "2022"
    areas = ["Downtown", "Kitsilano", "Sunset"]
    place_names = ["Carnegie Community Centre", "Kitsilano Neighbourhood House", "John Oliver Secondary School"]
    type_names = ["Community Centre", "Community Centre", "School"]

    def test_valid_input(self):
        area_objects = create_area_objects_list(self.year, self.areas, self.place_names)
        self.assertEqual(len(area_objects), 3)
        self.assertEqual(area_objects[0].year, self.year)
        self.assertEqual(area_objects[0].area, self.areas[0])
        self.assertEqual(area_objects[0].type_name, "Community Centre")
        self.assertEqual(area_objects[1].year, self.year)
        self.assertEqual(area_objects[1].area, self.areas[1])
        self.assertEqual(area_objects[1].type_name, "Community Centre")
        self.assertEqual(area_objects[2].year, self.year)
        self.assertEqual(area_objects[2].area, self.areas[2])
        self.assertEqual(area_objects[2].type_name, "School")

    def test_invalid_year(self):
        with self.assertRaises(TypeError):
            create_area_objects_list(2022, self.areas, self.place_names)
        with self.assertRaises(ValueError):
            create_area_objects_list("", self.areas, self.place_names)
        with self.assertRaises(ValueError):
            create_area_objects_list("  ", self.areas, self.place_names)

    def test_invalid_areas(self):
        with self.assertRaises(TypeError):
            create_area_objects_list(self.year, "Downtown, Kitsilano, Sunset", self.type_names)
        with self.assertRaises(ValueError):
            create_area_objects_list(self.year, [], self.type_names)

    def test_invalid_place_names(self):
        with self.assertRaises(TypeError):
            create_area_objects_list(self.year, self.areas, "Carnegie Community Centre, Kitsilano Neighbourhood House, John Oliver Secondary School")
        with self.assertRaises(ValueError):
            create_area_objects_list(self.year, self.areas, [])
        with self.assertRaises(ValueError):
            create_area_objects_list(self.year, self.areas, ["Carnegie Community Centre", "Kitsilano Neighbourhood House"])

# test count_type_in_area
class TestCountTypeInArea(unittest.TestCase):

    area_objects = [
            Area("2022", "Downtown", "School"),
            Area("2022", "Downtown", "Community Centre"),
            Area("2022", "West End", "Church"),
            Area("2022", "Sunset", "School"),
            Area("2022", "Sunset", "Else"),
            Area("2022", "Kitsilano", "Community Centre"),
            Area("2022", "Kitsilano", "Church"),
            Area("2022", "Kerrisdale", "Else"),
        ]

    def test_count_type_in_area_valid_input(self):
        result1 = count_type_in_area(self.area_objects, "Downtown")
        self.assertEqual(result1, [1, 1, 0, 0])
        result2 = count_type_in_area(self.area_objects, "West End")
        self.assertEqual(result2, [0, 0, 1, 0])
        result3 = count_type_in_area(self.area_objects, "Sunset")
        self.assertEqual(result3, [1, 0, 0, 1])
        result4 = count_type_in_area(self.area_objects, "Kitsilano")
        self.assertEqual(result4, [0, 1, 1, 0])
        result5 = count_type_in_area(self.area_objects, "Kerrisdale")
        self.assertEqual(result5, [0, 0, 0, 1])

    def test_count_type_in_area_invalid_input(self):
        with self.assertRaises(TypeError):
            count_type_in_area(self.area_objects, 123)
        with self.assertRaises(TypeError):
            count_type_in_area(self.area_objects, ["Downtown"])
        with self.assertRaises(ValueError):
            count_type_in_area([], "Downtown")

def main():
    """
    Ran 22 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()