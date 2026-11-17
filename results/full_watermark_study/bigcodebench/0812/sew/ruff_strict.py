import re
import tarfile
from pathlib import Path

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"


def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.

    Parameters:
    - directory: The directory to search for files matching a specified pattern. The function will iterate over all files within this directory, including subdirectories.
    - file_pattern: A regular expression pattern used to match filenames. Files whose names match this pattern will be added to an archive (tar file).

    Returns:
    - str: Path to the created tar file.

    Requirements:
    - re
    - pathlib
    - tarfile

    Example:
    >>> f_680('/path/to/source', '/path/to/target')
    """
    tar_path = Path(directory) / "archive.tar"
    with tarfile.open(tar_path, "w") as tar:
        for path in Path(directory).rglob("*"):
            if re.match(file_pattern, path.name):
                try:
                    tar.add(path, arcname=path.relative_to(directory))
                except PermissionError as e:
                    print(f"Skipping {path} due to permission error: {e}")
    return str(tar_path)
