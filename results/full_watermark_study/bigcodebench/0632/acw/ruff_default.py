import time

import pandas as pd

OUTPUT_DIR = "./output"


def task_func(df: pd.DataFrame, filename: str) -> str:
    """
    Write a Pandas DataFrame into a JSON Lines file and save it in a specified directory.

    Parameters:
    - df (pd.DataFrame): A Pandas DataFrame to be saved.
    - filename (str): The filename of the JSON Lines file to be saved.

    Returns:
    - str: The full path where the JSON Lines file was saved.

    Requirements:
    - pandas
    - time

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> 'data.jsonl' in task_func(df, 'data.jsonl')
    True
    """
    start_time = time.time()
    # Ensure the data directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    file_path = os.path.join(OUTPUT_DIR, filename)

    # Save DataFrame as JSON Lines
    with open(file_path, "w") as file:
        for record in df.to_dict(orient="records"):
            json.dump(record, file)
            file.write("\n")
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return os.path.abspath(file_path)
