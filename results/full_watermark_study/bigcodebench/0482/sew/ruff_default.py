import random
import re

import pandas as pd


def task_func(data_list, seed=None):
    """
    Apply a random operation (remove, replace, shuffle, or randomize) to substrings in a list of strings.

    This function processes a list of comma-separated strings by applying one of four random operations to
    their substrings: remove, replace, shuffle, or randomize. Here, a substring refers to the individual
    items in the string that are separated by commas, sensitive to leading/trailing whitespace, i.e.
    'apple' != 'apple ', and sensitive to case, i.e. 'APPLE' != 'aPPLE'.

    The choice of operation and the substrings it affects are determined randomly. The operations are:
    - Remove: Randomly selects and removes a substring.
              If a string contains only one substring, no 'remove' operation is applied.
    - Replace: Randomly selects a substring and replaces it with 'random_string'.
    - Shuffle: Randomly shuffles the order of the substrings.
    - Randomize: Assigns a new, random order to the substrings.

    Finally, the function returns a DataFrame with column 'Original String' containing the input strings
    and the 'Modified String' column containing the strings after applying the random operation.

    Parameters:
    - data_list (list): The list of strings. If empty, function will return a DataFrame with the expected
                        columns that is otherwise empty.
    - seed (int, optional): A seed for the random operations to ensure reproducibility. Default is None.

    Returns:
    df (pd.DataFrame): DataFrame containing original and modified strings.

    Requirements:
    - pandas
    - random
    - re

    Example:
    >>> task_func(['lamp, bag, mirror', 'table, chair, bag, lamp'], seed=0)
               Original String          Modified String
    0        lamp, bag, mirror        bag, lamp, mirror
    1  table, chair, bag, lamp  lamp, chair, bag, table
    """
    random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        operation = random.choice(["remove", "replace", "shuffle", "randomize"])
        if operation == "remove":
            if len(substrings) > 1:
                random_substring = random.choice(substrings)
                substrings.remove(random_substring)
                modified_s = ", ".join(substrings)
            else:
                modified_s = s
        elif operation == "replace":
            random_substring_index = random.choice(range(len(substrings)))
            substrings[random_substring_index] = "random_string"
            modified_s = ", ".join(substrings)
        elif operation == "shuffle":
            random.shuffle(substrings)
            modified_s = ", ".join(substrings)
        elif operation == "randomize":
            random_positions = random.sample(range(len(substrings)), len(substrings))
            modified_s = ", ".join([substrings[i] for i in random_positions])
        modified_strings.append(modified_s)

    df["Modified String"] = modified_strings

    return df
