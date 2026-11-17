import random

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS, MIN_VALUE = 5000, 0.0
MAX_VALUE = 10.0


def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating point numbers, truncate each value to 3 decimal places and normalize the data using standard scaling (mean = 0, std = 1).

    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.

    Returns:
    DataFrame: A pandas DataFrame with the normalized data.

    Raises:
    If max_value is less than min_value, a ValueError is raised.

    Note:
    - The function use "Normalized Value" for the column name in the DataFrame that being returned.

    Requirements:
    - pandas
    - random
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> random.seed(0)
    >>> normalized_data = task_func(5000, 5, 5)
    >>> print(normalized_data['Normalized Value'][0])
    0.0
    """
    if min_value > max_value:
        raise ValueError()

    data = []
    for _ in range(n_data_points):
        data.append(round(random.uniform(min_value, max_value), 3))
    data_df = pd.DataFrame(data, columns=["Value"])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[["Value"]])

    return pd.DataFrame(normalized_data, columns=["Normalized Value"])
