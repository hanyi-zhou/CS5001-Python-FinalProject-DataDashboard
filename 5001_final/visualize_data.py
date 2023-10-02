"""
CS 5001
Spring 2023
Final Project - visualize_data
Hanyi(Hanna) Zhou

A visualization file to visualize the analyzed data.
"""

import matplotlib.pyplot as plt

from constants import YEAR_2014, YEAR_2018, YEAR_2022, TYPE_COUNT_INDEX, FIG_SIZE, BAR_WIDTH, FIG1_X_LABEL, TYPE_RATIO_INDEX, RATIO_TEXT_POSITION, PLACE_TYPES, FIG2_X_LABEL, FIG2_Y_LABEL, LENGTH_OF_TWO, LENGTH_OF_THREE, LENGTH_OF_FOUR, FIRST_ITEM, SECOND_ITEM, HA, VA

def display_type_number_and_ratio_bar_chart(type_number_and_ratios_dict, input_type):
    """
    Displays a bar chart with the number of a given voting place type and its ratio to the total number
    of voting places for each year in a dictionary.

    Parameters:
        type_number_and_ratios_dict (dict): A dictionary where the keys are years (integers) and the values
            are lists containing two items: the number of voting places of the input type (int) and the
            ratio of the input type to the total number of voting places (string).
        input_type (str): A string representing the input type of voting place.

    Raises:
        TypeError: If type_number_and_ratios_dict is not a dictionary, or if input_type is not a string.
        ValueError: If type_number_and_ratios_dict is empty or is not length of 3,
                    or if any of the keys in type_number_and_ratios_dict is not in ['2014', '2018', '2022'].
        TypeError: If any of the values in type_number_and_ratios_dict is not a list, or if the first
                   item in any of the lists is not an integer or the second item is not a string.
    """
    if not isinstance(type_number_and_ratios_dict, dict):
        raise TypeError("type_number_and_ratios_dict must be a dictionary.")
    if not isinstance(input_type, str):
        raise TypeError("input_type must be a string.")
    if not type_number_and_ratios_dict:
        raise ValueError("type_number_and_ratios_dict cannot be empty.")
    if len(type_number_and_ratios_dict) != LENGTH_OF_THREE:
        raise ValueError("type_number_and_ratios_dict must be length of 3.")
    for year, type_number_and_ratio in type_number_and_ratios_dict.items():
        if year not in [YEAR_2014, YEAR_2018, YEAR_2022]:
            raise ValueError("Keys in type_number_and_ratios_dict must be '2014', '2018' or '2022'.")
        if not isinstance(type_number_and_ratio, list):
            raise TypeError("Values in type_number_and_ratios_dict must be lists.")
        if len(type_number_and_ratio) != LENGTH_OF_TWO:
            raise ValueError("Values in type_number_and_ratios_dict must be length of 2.")
        if not isinstance(type_number_and_ratio[FIRST_ITEM], int) or not isinstance(type_number_and_ratio[SECOND_ITEM], str):
            raise TypeError("The first item in list must be an interger and the second item in list must be a string.")
    # extract years and type counts
    years = list(type_number_and_ratios_dict.keys())
    type_counts = [val[TYPE_COUNT_INDEX] for val in type_number_and_ratios_dict.values()]

    # create a bar chart
    plt.figure(figsize=FIG_SIZE)
    x = range(len(years))
    plt.bar(x, type_counts, width=BAR_WIDTH)

    # set x and y and the title
    plt.xticks(x, years)
    plt.xlabel(FIG1_X_LABEL)
    plt.ylabel(f'{input_type.title()} Number')
    plt.title(f'Voting Place Type [{input_type.title()}] Number and Ratio to Total Number Changed')

    # add texts on the bar chart
    for i, num in enumerate(type_counts):
        plt.text(x[i], num, f'{num}', ha=HA, va=VA)
    for i, val in enumerate(type_number_and_ratios_dict.values()):
        label = val[TYPE_RATIO_INDEX]
        plt.text(x[i], type_counts[i]+RATIO_TEXT_POSITION, label, ha=HA)

    # show the chart
    plt.show()

def display_area_type_number_bar_chart(type_counts_in_area_dict, input_area):
    """
    Display a grouped bar chart showing the number of voting place types in an area for each year.

    Parameters:
        type_counts_in_area_dict (dict): A dictionary where the keys are the years, and the values are lists of integers
                                         representing the number of each voting place type in the area for that year.
        input_area (str): The name of the area for which the chart is being displayed.

    Raises:
        TypeError: If type_counts_in_area_dict is not a dictionary or input_area is not a string.
        TypeError: If any value in type_counts_in_area_dict is not list of integers.
        ValueError: If any key in type_counts_in_area_dict is not in ['2014', '2018', '2022'].
                    If any value in type_counts_in_area_dict is not length of 4.
        ValueError: If type_counts_in_area_dict is empty or is not length of 3.
    """
    if not isinstance(type_counts_in_area_dict, dict):
        raise TypeError("type_counts_in_area_dict must be a dictionary.")
    if not isinstance(input_area, str):
        raise TypeError("input_area must be a string.")
    if not type_counts_in_area_dict:
        raise ValueError("type_counts_in_area_dict cannot be empty.")
    if len(type_counts_in_area_dict) != LENGTH_OF_THREE:
        raise ValueError("type_counts_in_area_dict must be length of 3.")
    for year, type_number in type_counts_in_area_dict.items():
        if year not in [YEAR_2014, YEAR_2018, YEAR_2022]:
            raise ValueError("Keys in type_counts_in_area_dict must be '2014', '2018' or '2022'.")
        if not isinstance(type_number, list):
            raise TypeError("Values in type_counts_in_area_dict must be lists.")
        if not all(isinstance(num, int) for num in type_number):
            raise TypeError("Values in type_counts_in_area_dict must be lists of integers.")
        if len(type_number) != LENGTH_OF_FOUR:
            raise ValueError("Values in type_counts_in_area_dict must be length of 4.")

    # create a gouped bar chart
    plt.figure(figsize=FIG_SIZE)
    years = list(type_counts_in_area_dict.keys())
    area_type_number = list(type_counts_in_area_dict.values())

    # iterates over each year in the years list and creates a list of x coordinates for the bars in that year
    for i in range(len(years)):
        bar_x = []
        # the x coordinates are spaced apart by BAR_WIDTH, and are shifted to the right based on the current year index i
        for x in range(len(area_type_number[i])):
            bar_x.append(x + i * BAR_WIDTH)
        # for each x coordinate in bar_x, a bar is created with the corresponding value
        plt.bar(bar_x, area_type_number[i], width=BAR_WIDTH, label=years[i])
        # for each bar, a text label is added at the top of the bar with the value of the bar
        for j in range(len(bar_x)):
            plt.text(bar_x[j], area_type_number[i][j], str(area_type_number[i][j]), ha=HA, va=VA)

    # add x ticks and the title
    x_ticks = []
    for i in range(len(area_type_number[0])):
        tick = i + BAR_WIDTH * (len(years) - 1) / 2
        x_ticks.append(tick)
    plt.xticks(x_ticks, PLACE_TYPES)

    plt.xlabel(FIG2_X_LABEL)
    plt.ylabel(FIG2_Y_LABEL)
    plt.legend()

    plt.title(f'Voting Place Types Number Changed in {input_area.title()}')

    # show the chart
    plt.show()