import numpy as np
import pandas as pd

# Constants
COLUMNS = ["Column1", "Column2", "Column3", "Column4", "Column5"]


def task_func(length):
    """
    Generate a Pandas DataFrame with specified length and random data and then record the data.

    Parameters:
    length (int): The length of the DataFrame to be generated.

    Returns:
    DataFrame: A pandas DataFrame with random data.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> df = task_func(5)
    >>> df.shape
    (5, 5)
    """

    data = np.random.randint(0, 100, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    return df
