"""
CS 5001
Spring 2023
Final Project - test_get_data
Hanyi(Hanna) Zhou

A file to test get_data functions.
"""
import unittest, requests
from get_data import get_csv_from_url, get_data_list, clean_lists

from constants import URL_2014, CSV_2014_LINES

# test get_csv_from_url
class TestGetCsvFromUrl(unittest.TestCase):

    def test_valid_url(self):
        url = URL_2014
        expected_csv_lines = CSV_2014_LINES
        actual_csv_lines = get_csv_from_url(url)
        self.assertEqual(actual_csv_lines, expected_csv_lines)

    def test_blank_string_url(self):
        url = ""
        with self.assertRaises(ValueError):
            get_csv_from_url(url)

    def test_whitespace_url(self):
        url = " "
        with self.assertRaises(ValueError):
            get_csv_from_url(url)

    def test_timeout_error(self):
        url = 'https://httpstat.us/504?sleep=5000'
        with self.assertRaises(requests.exceptions.Timeout):
            get_csv_from_url(url)

    def test_http_error(self):
        url = 'https://httpstat.us/404'
        with self.assertRaises(requests.exceptions.HTTPError):
            get_csv_from_url(url)

    def test_connection_error(self):
        url = 'https://not_a_real_url.com'
        with self.assertRaises(requests.exceptions.ConnectionError):
            get_csv_from_url(url)

    def test_general_error(self):
        url = 'https://httpbin.org/status/500'
        with self.assertRaises(requests.exceptions.RequestException):
            get_csv_from_url(url)

# test get_data_list
class TestGetDataList(unittest.TestCase):

    def test_valid_data_extraction(self):
        csv_lines = ['Header;Column1;Column2', 'Row1;1;4', 'Row2;2;5', 'Row3;3;6']
        expected_data_list = ['1', '2', '3']
        actual_data_list = get_data_list(csv_lines, 1)
        self.assertEqual(actual_data_list, expected_data_list)

    def test_empty_csv_lines(self):
        csv_lines = []
        with self.assertRaises(ValueError):
            get_data_list(csv_lines, 0)

    def test_negative_column_index(self):
        csv_lines = ['Header;Column1;Column2', 'Row1;1;4', 'Row2;2;5', 'Row3;3;6']
        with self.assertRaises(ValueError):
            get_data_list(csv_lines, -1)

    def test_invalid_column_index(self):
        csv_lines = ['Header;Column1;Column2', 'Row1;1;4', 'Row2;2;5', 'Row3;3;6']
        with self.assertRaises(IndexError):
            get_data_list(csv_lines, 3)

    def test_non_list_csv_lines(self):
        csv_lines = 'not a list'
        with self.assertRaises(TypeError):
            get_data_list(csv_lines, 0)

    def test_non_int_column_index(self):
        csv_lines = 'not an integer'
        with self.assertRaises(TypeError):
            get_data_list(csv_lines, 1)

# test clean_lists
class TestCleanLists(unittest.TestCase):

    def test_with_no_blank_strings_in_the_areas_list(self):
        areas = ["Downtown", "Strathcona", "Sunset"]
        place_names = ["Jubilee House", "Strathcona Community Centre", "Henderson Annex"]
        expected_areas = ["Downtown", "Strathcona", "Sunset"]
        expected_place_names = ["Jubilee House", "Strathcona Community Centre", "Henderson Annex"]
        cleaned_areas, cleaned_place_names = clean_lists(areas, place_names)
        self.assertEqual(cleaned_areas, expected_areas)
        self.assertEqual(cleaned_place_names, expected_place_names)

    def test_with_blank_strings_in_the_areas_list(self):
        areas = ["Downtown", "Strathcona", "", "Sunset", ""]
        place_names = ["Jubilee House", "Strathcona Community Centre", "Carey Theological College", "Henderson Annex", "University Hill Secondary School"]
        expected_areas = ["Downtown", "Strathcona", "Sunset"]
        expected_place_names = ["Jubilee House", "Strathcona Community Centre", "Henderson Annex"]
        cleaned_areas, cleaned_place_names = clean_lists(areas, place_names)
        self.assertEqual(cleaned_areas, expected_areas)
        self.assertEqual(cleaned_place_names, expected_place_names)

    def test_with_empty_lists(self):
        areas = []
        place_names = []
        with self.assertRaises(ValueError):
            clean_lists(areas, place_names)

    def test_with_lists_of_different_lengths(self):
        areas = ["Downtown", "Strathcona"]
        place_names = ["Jubilee House", "Strathcona Community Centre", "Henderson Annex"]
        with self.assertRaises(ValueError):
            clean_lists(areas, place_names)

    def test_with_non_list_argument(self):
        areas = "Downtown, Strathcona"
        place_names = ["Jubilee House", "Strathcona Community Centre", "Henderson Annex"]
        with self.assertRaises(TypeError):
            clean_lists(areas, place_names)

def main():
    """
    Ran 18 tests.
    All passed.
    """
    unittest.main(verbosity=1)

if __name__ == '__main__':
    main()