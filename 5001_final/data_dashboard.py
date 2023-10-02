"""
CS 5001
Spring 2023
Final Project - data_dashboard
Hanyi(Hanna) Zhou

A driver file, when executed, will download the data, parse the data into objects, do an analysis, and visualize the result.

Mainly get two user inputs and display two charts:
1. When the user inputs a voting place type among School/Community Centre/Church/Else, the program will display a
bar chart showing the number and ratio to the total changed of that type for the years 2014, 2018 and 2022.
2. When the user inputs an area name chosen from an area name list, the program will change to display a grouped
bar chart showing the number changed of voting places of 4 different types School/Community Centre/Church/Else in
that area for the years 2014, 2018 and 2022.
"""

from get_data import get_csv_from_url, get_data_list, clean_lists
from get_user_input import get_type_input, get_area_input, create_areas_name_list
from type_number_and_ratio_analysis import create_place_objects_list, count_type, calculate_type_ratio
from area_type_number_analysis import create_area_objects_list, count_type_in_area
from visualize_data import display_type_number_and_ratio_bar_chart, display_area_type_number_bar_chart

from constants import URL_2014, URL_2018, URL_2022, PLACE_NAME_COLUMN_INDEX_2014, PLACE_NAME_COLUMN_INDEX_2018, PLACE_NAME_COLUMN_INDEX_2022, YEAR_2014, YEAR_2018, YEAR_2022, AREA_COLUMN_INDEX_2014, AREA_COLUMN_INDEX_2018, AREA_COLUMN_INDEX_2022

def main():
    try:
        # download datasets
        csv_2014 = get_csv_from_url(URL_2014)
        csv_2018 = get_csv_from_url(URL_2018)
        csv_2022 = get_csv_from_url(URL_2022)

        # user inputs a voting place type
        input_type = get_type_input()

        # read place names from datasets into data lists
        place_names_2014 = get_data_list(csv_2014, PLACE_NAME_COLUMN_INDEX_2014)
        place_names_2018 = get_data_list(csv_2018, PLACE_NAME_COLUMN_INDEX_2018)
        place_names_2022 = get_data_list(csv_2022, PLACE_NAME_COLUMN_INDEX_2022)

        # create VotingPlace objects lists
        place_objects_2014 = create_place_objects_list(YEAR_2014, place_names_2014)
        place_objects_2018 = create_place_objects_list(YEAR_2018, place_names_2018)
        place_objects_2022 = create_place_objects_list(YEAR_2022, place_names_2022)

        # analyze the type counts in each year
        type_count_2014 = count_type(place_objects_2014, input_type)
        type_count_2018 = count_type(place_objects_2018, input_type)
        type_count_2022 = count_type(place_objects_2022, input_type)

        # analyze the type ratios in each year
        type_ratio_2014 = calculate_type_ratio(place_objects_2014, type_count_2014)
        type_ratio_2018 = calculate_type_ratio(place_objects_2018, type_count_2018)
        type_ratio_2022 = calculate_type_ratio(place_objects_2022, type_count_2022)

        # store the first analysis result into a dictionary
        type_number_and_ratio_dict = {YEAR_2014:[type_count_2014, type_ratio_2014], YEAR_2018:[type_count_2018, type_ratio_2018], YEAR_2022:[type_count_2022, type_ratio_2022]}

        # display the first analysis result in a bar chart
        display_type_number_and_ratio_bar_chart(type_number_and_ratio_dict, input_type)

        # read area names from CSVs into data lists
        areas_2014 = get_data_list(csv_2014, AREA_COLUMN_INDEX_2014)
        areas_2018 = get_data_list(csv_2018, AREA_COLUMN_INDEX_2018)
        areas_2022 = get_data_list(csv_2022, AREA_COLUMN_INDEX_2022)

        # clean data preparing for the second user input and analysis
        new_areas_2014, new_place_names_2014 = clean_lists(areas_2014, place_names_2014)
        new_areas_2018, new_place_names_2018 = clean_lists(areas_2018, place_names_2018)
        new_areas_2022, new_place_names_2022 = clean_lists(areas_2022, place_names_2022)

        # create an area name list
        print()
        areas_set = create_areas_name_list(new_areas_2014, new_areas_2018, new_areas_2022)

        # display the area name list, user inputs an area
        input_area = get_area_input(areas_set)

        # create Area objects lists
        area_objects_2014 = create_area_objects_list(YEAR_2014, new_areas_2014, new_place_names_2014)
        area_objects_2018 = create_area_objects_list(YEAR_2018, new_areas_2018, new_place_names_2018)
        area_objects_2022 = create_area_objects_list(YEAR_2022, new_areas_2022, new_place_names_2022)

        # analyze each type counts in the area
        type_counts_in_area_2014 = count_type_in_area(area_objects_2014, input_area)
        type_counts_in_area_2018 = count_type_in_area(area_objects_2018, input_area)
        type_counts_in_area_2022 = count_type_in_area(area_objects_2022, input_area)

        # store the second analysis result into a dictionary
        type_counts_in_area_dict = {YEAR_2014: type_counts_in_area_2014, YEAR_2018: type_counts_in_area_2018, YEAR_2022: type_counts_in_area_2022}

        # display the second analysis result in a grouped bar chart
        display_area_type_number_bar_chart(type_counts_in_area_dict, input_area)

    except TypeError as e:
        print(f"TypeError occurred: {e}.")
    except ValueError as e:
        print(f"ValueError occurred: {e}.")
    except NameError as e:
        print(f"NameError occurred: {e}.")
    except Exception as e:
        print(f"Other error occurred: {e}.")

if __name__ == '__main__':
    main()