import math
from random import randint

import pandas as pd


def task_func(cities_list):
    """
    Generate a DataFrame with population data for a list of cities. The population is generated randomly
    and rounded up to the next thousand.

    Requirements:
    - pandas
    - math
    - random

    Parameters:
    cities_list (list): A list of city names.

    Returns:
    DataFrame: A pandas DataFrame with columns 'City' and 'Population', containing population data for the cities.

    Example:
    >>> cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    >>> pop_data = task_func(cities)
    >>> type(pop_data)
    <class 'pandas.core.frame.DataFrame'>
    """
    population_data = list()

    for city in cities_list:
        population = 1000 * math.ceil(randint(1000000, 20000000) / 1000.0)
        population_data.append([city, population])

    population_df = pd.DataFrame(population_data, columns=["City", "Population"])

    return population_df
