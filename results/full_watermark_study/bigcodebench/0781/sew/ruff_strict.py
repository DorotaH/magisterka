import os
from datetime import datetime


def task_func(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.

    Parameters:
    - filepath (str): The path to the file.

    Returns:
    - dict: A dictionary containing the size (in bytes) and last modification
          date of the file in the format '%Y-%m-%d %H:%M:%S'.

    Requirements:
    - os
    - datetime

    Example:
    >>> task_func('/path/to/file.txt')
    {'size': '1024 bytes', 'last_modified': '2022-01-01 12:30:45'}
    """
    try:
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        mtime = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    except OSError as e:
        raise Exception(f"Error: {e}")

    return {"size": f"{size} bytes", "last_modified": mtime}
