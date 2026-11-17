import glob
import os
import shutil


def task_func(directory, archive_dir="archive"):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.

    Parameters:
    directory (str): The directory where the JSON files are located.
    archive_dir (str): The directory to which the JSON files will be archived. Defaults to 'archive'.

    Returns:
    tuple: A tuple containing a boolean value and a list of error messages.
            The boolean is True if all files are successfully moved, and False otherwise.
            The list contains error messages for each file that failed to move.

    Requirements:
    - os
    - glob
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file1.json', 'file2.json', 'file3.json']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> backup_dir = tempfile.mkdtemp()
    >>> task_func(temp_dir, backup_dir)
    (True, [])
    """
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    json_files = glob.glob(os.path.join(directory, "*.json"))
    error_messages = []

    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f"Unable to move {json_file} due to {e!s}"
            error_messages.append(error_message)

    return not error_messages, error_messages
