import random
import re

import pandas as pd


def task_func(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.

    This function takes a list of comma-separated strings and splits each into substrings.
    It extracts substrings based on commas, removing leading and trailing whitespaces
    from each. Then, it shuffles these processed substrings within each string, and
    returns a pandas DataFrame with two columns: "Original String" and "Shuffled String".

    Parameters:
    data_list (list): The list of comma-separated strings.
    seed (int, optional): Seed for the random number generator. Default is None.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Original String' and 'Shuffled String'.

    Requirements:
    - pandas
    - random
    - re

    Example:
    >>> task_func(['lamp, bag, mirror', 'table, chair'], seed=42)
         Original String    Shuffled String
    0  lamp, bag, mirror  bag, lamp, mirror
    1       table, chair       chair, table
    """
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    shuffled_strings = []
    for s in data_list:
        substrings = re.split(r"\s*,\s*", s)
        random.shuffle(substrings)
        shuffled_s = ", ".join(substrings)
        shuffled_strings.append(shuffled_s)

    df["Shuffled String"] = shuffled_strings

    return df
