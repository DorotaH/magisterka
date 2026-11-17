import os
from pathlib import Path
import glob
import shutil


def task_func(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory,
    handling naming conflicts by renaming duplicates.

    Parameters:
    - source_directory (str): The absolute or relative path of the source directory.
    - target_directory (str): The absolute or relative path of the target directory.
                              This function will create it if it does not exist.

    Returns:
    - int: The number of files successfully moved.

    Raises:
    - FileNotFoundError: If source_directory does not exist.

    Requirements:
    - os
    - pathlib
    - glob
    - shutil

    Notes:
    - This function scans the source directory recursively to find files.
    - Files are filtered by the extensions: ".txt", ".docx", ".xlsx", ".csv".
    - Renaming of files due to naming conflicts follows the pattern '<original_name>-n.<extension>'.

    Examples:
    >>> task_func('./source_folder', './target_folder')
    3
    >>> task_func('./empty_folder', './target_folder')
    0
    """
    moved_files = 0

    if not os.path.exists(source_directory):
        raise FileNotFoundError("source_directory must exist.")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for extension in [".txt", ".docx", ".xlsx", ".csv"]:
        filepaths = glob.glob(
            os.path.join(source_directory, "**", "*" + extension), recursive=True
        )
        for filepath in filepaths:
            filename = Path(filepath).name
            stem = Path(filepath).stem
            target_filepath = os.path.join(target_directory, filename)

            count = 1
            while os.path.exists(target_filepath):
                new_filename = f"{stem}-{count}{extension}"
                target_filepath = os.path.join(target_directory, new_filename)
                count += 1

            shutil.move(filepath, target_filepath)
            moved_files += 1

    return moved_files
