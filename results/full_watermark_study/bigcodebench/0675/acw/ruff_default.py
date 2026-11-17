import os
import random


def task_func(directory, n_files):
    """
    Create n random text files in a specific directory, write a random string to each file, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n_files (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random

    Example:
    >>> task_func('/path/to/directory', 5)
    '/path/to/directory'
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i + 1}.txt")

        with open(filename, "w") as file:
            file.write(str(random.randint(1, 100)))
            file.seek(0)

    return directory
