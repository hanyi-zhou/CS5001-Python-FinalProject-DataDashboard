"""
CS 5001
Spring 2023
Final Project - get_data
Hanyi(Hanna) Zhou

A file to download a CSV file from a given URL, clean and get data list.
"""

import requests
from constants import URL_2014, URL_2018, URL_2022, SEMICOLON, HEADER_INDEX, BLANK_STRING

# download csv from url
def get_csv_from_url(url):
    """
    Downloads a CSV file from a URL and returns its content as a list of lines.

    Parameters:
        url (str): The URL of the CSV file to download.

    Returns:
        csv_lines (list): A list of lines from the downloaded CSV file.

    Raises:
        TypeError: If the URL is not a string.
        ValueError: If the URL is a blank string or contains whitespace.
        requests.exceptions.Timeout: If a timeout occurs while accessing the URL.
        requests.exceptions.HTTPError: If an HTTP error occurs while accessing the URL.
        requests.exceptions.ConnectionError: If a connection error occurs while accessing the URL.
        requests.exceptions.RequestException: If a general request error occurs while accessing the URL.
    """
    if not isinstance(url, str):
        raise TypeError("url must be a string.")
    if not url or url.isspace():
        raise ValueError("url is a blank string or contains whitespace.")
    try:
        response = requests.get(url, timeout=1)
        # raise HTTPError
        response.raise_for_status()
        content = response.text
        # split rows of csv file into a list like ['vd;facility_name;facility_address;advance_only;location;local_area;geom;geo_point_2d', ...]
        csv_lines = content.splitlines()

    # handle requests errors
    except requests.exceptions.Timeout as e:
        raise requests.exceptions.Timeout(f"Error: Timeout occurred while accessing URL: {url}. {e}")
    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError(f"Error: HTTP error occurred while accessing URL: {url}. Status code: {response.status_code}. {e}")
    except requests.exceptions.ConnectionError as e:
        raise requests.exceptions.ConnectionError(f"Error: Connection error occurred while accessing URL: {url}. {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error: Failed to download data from URL: {url}. {e}")

    return csv_lines

# extract a column of data as a list
def get_data_list(csv_lines, column_index):
    """
    Extracts a column of data from a CSV file and returns it as a list.

    Parameters:
        csv_lines (list): A list of strings representing the lines of the CSV file.
        column_index (int): The index of the column to extract.

    Returns:
         data_list (list): A list of strings representing the data in the specified column.

    Raises:
        TypeError: If csv_lines is not a list or column_index is not an integer.
        ValueError: If csv_lines is empty or column_index is negative.
        IndexError: If column_index is out of range for a line in csv_lines.
    """
    if not isinstance(csv_lines, list):
        raise TypeError("csv_lines must be a list.")
    if not isinstance(column_index, int):
        raise TypeError("column_index must be an integer.")
    if not csv_lines:
        raise ValueError("csv_lines cannot be empty.")
    if column_index < 0:
        raise ValueError("column_index cannot be negative.")
    # delete the header
    csv_lines_copy = csv_lines.copy()
    csv_lines_copy.pop(HEADER_INDEX)
    # create a data list of the given column index
    data_list = []
    for line in csv_lines_copy:
        # split each line with semicolon
        line = line.split(SEMICOLON)
        if column_index >= len(line):
            raise IndexError("column_index out of range.")
        # append the given column data into the data list
        data_list.append(line[column_index])
    return data_list

# delete the blank strings in areas list and the corresponding place names in places list
def clean_lists(areas, place_names):
    """
    Deletes the blank strings in the areas list and the corresponding place names in the places list.

    Parameters:
        areas (list): A list of strings representing the areas.
        place_names (list): A list of strings representing the place names.

    Returns:
        new_areas, new_place_names (a tuple containing two lists): the cleaned areas list and the corresponding cleaned place names list.

    Raises:
        TypeError: If areas or place_names is not a list.
        ValueError: If areas or place_names is empty, or they have different lengths.
    """
    if not isinstance(areas, list):
        raise TypeError("areas must be a list.")
    if not isinstance(place_names, list):
        raise TypeError("place_names must be a list.")
    if not areas or not place_names:
        raise ValueError("areas and place_names cannot be empty.")
    if len(areas) != len(place_names):
        raise ValueError("areas and place_names must have the same length.")
    new_areas = []
    new_place_names = []
    for i in range(len(areas)):
        if areas[i] != BLANK_STRING:
            new_areas.append(areas[i])
            new_place_names.append(place_names[i])
    return new_areas, new_place_names