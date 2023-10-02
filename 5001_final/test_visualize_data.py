"""
CS 5001
Spring 2023
Final Project - test_visualize_data
Hanyi(Hanna) Zhou

A file to test visualize_data functions.
"""

import unittest
from unittest.mock import patch

from visualize_data import display_type_number_and_ratio_bar_chart, display_area_type_number_bar_chart

# test display_type_number_and_ratio_bar_chart
class TestDisplayTypeNumberAndRatioBarChart(unittest.TestCase):

    def setUp(self):
        self.type_number_and_ratios_dict = {"2014": [1, "10.00%"],
                                       "2018": [2, "20.00%"],
                                       "2022": [3, "30.00%"]}
        self.input_type = "school"

    def test_valid_input(self):
        with patch("matplotlib.pyplot.show") as mock_show:
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, self.input_type)
            mock_show.assert_called_once_with()

    def test_invalid_type_number_and_ratios_dict(self):
        with self.assertRaises(TypeError):
            display_type_number_and_ratio_bar_chart("not a dictionary", self.input_type)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, 123)

    def test_invalid_key_in_type_number_and_ratios_dict(self):
        self.type_number_and_ratios_dict["2023"] = [4, "50.00%"]
        with self.assertRaises(ValueError):
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, self.input_type)

    def test_invalid_value_in_type_number_and_ratios_dict(self):
        self.type_number_and_ratios_dict["2022"] = [3, 5]
        with self.assertRaises(TypeError):
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, self.input_type)

    def test_invalid_length_in_type_number_and_ratios_dict(self):
        self.type_number_and_ratios_dict["2022"] = [3]
        with self.assertRaises(ValueError):
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, self.input_type)

    def test_empty_type_number_and_ratios_dict(self):
        with self.assertRaises(ValueError):
            display_type_number_and_ratio_bar_chart({}, self.input_type)

    def test_invalid_length_in_type_number_and_ratios_dict(self):
        self.type_number_and_ratios_dict.update({"2023": [4, '40.00%']})
        with self.assertRaises(ValueError):
            display_type_number_and_ratio_bar_chart(self.type_number_and_ratios_dict, self.input_type)

# test display_area_type_number_bar_chart
class TestDisplayAreaTypeNumberBarChart(unittest.TestCase):

    def setUp(self):
        self.type_counts_in_area_dict = {"2014": [1, 2, 3, 4],
                                        "2018": [2, 3, 4, 5],
                                        "2022": [3, 4, 5, 6]}
        self.input_area = "downtown"

    def test_valid_input(self):
        with patch("matplotlib.pyplot.show") as mock_show:
            display_area_type_number_bar_chart(self.type_counts_in_area_dict, self.input_area)
            mock_show.assert_called_once()

    def test_invalid_type_counts_in_area_dict(self):
        with self.assertRaises(TypeError):
            display_area_type_number_bar_chart("not a dictionary", self.input_area)

    def test_invalid_input_area(self):
        with self.assertRaises(TypeError):
            display_area_type_number_bar_chart(self.type_counts_in_area_dict, 123)

    def test_invalid_key_in_type_counts_in_area_dict(self):
        self.type_counts_in_area_dict["2023"] = [4, 5, 6, 7]
        with self.assertRaises(ValueError):
            display_area_type_number_bar_chart(self.type_counts_in_area_dict, self.input_area)

    def test_invalid_value_in_type_counts_in_area_dict(self):
        self.type_counts_in_area_dict["2022"] = [3, "four", 5, 6]
        with self.assertRaises(TypeError):
            display_area_type_number_bar_chart(self.type_counts_in_area_dict, self.input_area)

    def test_invalid_length_in_type_counts_in_area_dict(self):
        self.type_counts_in_area_dict["2022"] = [3, 4, 5]
        with self.assertRaises(ValueError):
            display_area_type_number_bar_chart(self.type_counts_in_area_dict, self.input_area)

    def test_empty_type_counts_in_area_dict(self):
        with self.assertRaises(ValueError):
            display_area_type_number_bar_chart({}, self.input_area)

    def test_invalid_length_in_type_counts_in_area_dict(self):
        self.type_counts_in_area_dict.update({"2023": [5, 6, 7, 8]})
        with self.assertRaises(ValueError):
            display_type_number_and_ratio_bar_chart(self.type_counts_in_area_dict, self.input_area)

def main():
    """
    Ran 14 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()