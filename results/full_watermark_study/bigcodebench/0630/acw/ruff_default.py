import os

import pandas as pd

OUTPUT_DIR = "./output"


def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.

    Parameters:
    - df (DataFrame): A Pandas DataFrame to be saved.
    - filename (str): The filename of the JSON file where the DataFrame will be saved.
    - output_dir (str, optional): the ouput directory.

    Returns:
    str: The full file path where the DataFrame is saved.

    Requirements:
    - os
    - pandas

    Note:
    - The function manipulates a Pandas DataFrame and saves it as a JSON file.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> 'data.json' in task_func(df, 'data.json')
    True
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df_clean = df.where(pd.notnull(df), None)
    with open(file_path, "w") as f:
        df_clean.to_json(f, orient="records")
    return file_path
