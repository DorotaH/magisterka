import string
import random


def task_func(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter,
    while preserving the case and non-alphabetic characters of the original text.

    Parameters:
    - text (str): The input text to be transformed.
    - seed (int, optional): Random seed for reproducibility. Defaults to None (not set).

    Returns:
    - str: A transformed string with random letters replacing the alphabetic characters of the input text,
      preserving non-alphabetic characters and the original case.

    Requirements:
    - string
    - random

    Notes:
    - Alphabet replacements are chosen from ascii characters of the same case as the original.

    Example:
    >>> text = 'Hello, world!'
    >>> task_func(text, 0)
    'Mynbi, qpmzj!'
    """

    def replace_with_random_char(c):
        if c.isalpha():
            if c.islower():
                return random.choice(string.ascii_lowercase)
            else:
                return random.choice(string.ascii_uppercase)
        return c

    if seed is not None:
        random.seed(seed)
    return "".join(replace_with_random_char(c) for c in text)
