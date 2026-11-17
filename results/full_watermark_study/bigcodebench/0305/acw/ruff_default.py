import itertools
import random
from collections import Counter

# Constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def task_func(list_of_lists, seed=0):
    """
    Count the frequency of each letter in a list of lists. If a list is empty,
    fill it with a random sample from the alphabet, and then count the letters.

    Parameters:
    list_of_lists (list): The list of lists.
    seed (int): The seed for the random number generator. Defaults to 0.

    Returns:
    Counter: A Counter object with the frequency of each letter.

    Requirements:
    - collections.Counter
    - itertools
    - random.sample

    Example:
    >>> dict(task_func([['a', 'b', 'c'], [], ['d', 'e', 'f']]))
    {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'm': 1, 'y': 1, 'n': 1, 'i': 1, 'q': 1, 'p': 1, 'z': 1, 'j': 1, 't': 1}
    """
    random.seed(seed)
    flattened_list = list(itertools.chain(*list_of_lists))

    for list_item in list_of_lists:
        if list_item == []:
            flattened_list += random.sample(ALPHABET, 10)

    return Counter(flattened_list)
