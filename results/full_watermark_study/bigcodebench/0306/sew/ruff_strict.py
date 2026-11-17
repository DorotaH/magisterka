import logging
import os


def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.

    Parameters:
    directory (str): The directory path.

    Returns:
    tuple: A tuple containing two elements:
        - int: The number of files removed.
        - list: The names of the removed files.

    Raises:
    - If the specified directory does not exist the code would raise FileNotFoundError.

    Note:
    - Removed files are logged in 'jquery_removal.log' file.

    Requirements:
    - os
    - logging


    Example:
    >>> task_func("/path/to/directory")
    (3, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])  # Assuming 3 jQuery files were removed
    """

    # Configure logging
    logging.basicConfig(
        filename="jquery_removal.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Get all files in the directory
    files = os.listdir(directory)

    # Remove jQuery files
    removed_files = 0
    removed_file_names = []
    for file in files:
        if "jquery" in file and file.endswith(".js"):
            try:
                os.remove(os.path.join(directory, file))
                removed_files = removed_files + 1
                removed_file_names.append(file)
                logging.info(f"Removed jQuery file: {file}")
            except Exception as e:
                logging.error(f"Error while removing file {file}: {e}")

    return removed_files, removed_file_names
