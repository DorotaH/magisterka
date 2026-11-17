import os
import re
import hashlib

def task_func(path, delimiter):
    """
    Splits a file path by a specified delimiter, retaining the delimiter in the output, and computes the hash of each component if it is a file.
    
    Parameters:
    path (str): The file path to split.
    delimiter (str): The delimiter to use for splitting the path.

    Returns:
    list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
                 If the component is not a file, its hash will be None.

    Requirements:
    - os
    - re
    - hashlib

    Example:
    >>> task_func("Docs/src/file.txt", "/")
    [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', 'hash_value')]
    """
    path_components = re.split(f'({delimiter})', path)
    hashes = []

    for component in path_components:
        if not component:  # Remove empty components
            continue
        if component != delimiter and os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        else:
            hashes.append(None)

    return list(zip(path_components, hashes))
