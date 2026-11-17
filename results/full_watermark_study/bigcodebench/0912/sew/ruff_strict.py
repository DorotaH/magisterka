import itertools
from collections import Counter


def task_func(letters: list, repetitions: int) -> dict:
    """
    Count the frequency of each letter in a list after repeating it a given number of times.

    Parameters:
    - letters (list): A list of single-character strings representing letters.
    - repetitions (int): The number of times to repeat the list.

    Returns:
    Returns a dictionary where the keys are the letters and the values are their frequencies.

    Requirements:
    - collections.Counter
    - itertools

    Example:
    >>> task_func(['A', 'B', 'C'], 2)
    {'A': 2, 'B': 2, 'C': 2}
    >>> task_func(['A', 'B'], 3)
    {'A': 3, 'B': 3}
    """
    # Create a flattened list by repeating the original list
    flattened_list = list(itertools.chain(*[letters for _ in range(0, repetitions)]))

    # Count the occurrences of each letter in the flattened list
    counts = dict(Counter(flattened_list))

    return counts
