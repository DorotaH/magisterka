import numpy as np
import pandas as pd


def task_func(df, letter):
    """
    This function converts an input dictionary into a DataFrame, filters rows where 'Word' column values start with a
    specified letter, calculates the lengths of these words, and returns basic statistics (mean, median, mode) of the
    word lengths.

    Parameters:
    df (dict of list): A dictionary where the key 'Word' maps to a list of strings.
    letter (str): The letter to filter the 'Word' column.

    Returns:
    dict: A dictionary of mean, median, and mode of word lengths.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> df = {'Word': ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado']}
    >>> stats = task_func(df, 'a')
    >>> stats['mean'] > 0
    True
    >>> stats['median'] > 0
    True
    """
    df = pd.DataFrame(df)
    regex = "^" + letter
    filtered_df = df[df["Word"].str.contains(regex, regex=True)]
    word_lengths = filtered_df["Word"].str.len()
    statistics = {
        "mean": np.mean(word_lengths),
        "median": np.median(word_lengths),
        "mode": word_lengths.mode().values[0],
    }

    return statistics
