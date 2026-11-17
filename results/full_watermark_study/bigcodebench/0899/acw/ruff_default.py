import random

import numpy as np


def task_func(length=10000, seed=0):
    """
    Generates a random walk of a specified length. A random walk is a path that consists of a series of random steps
    on some mathematical space. In this case, the steps are either +1 or -1, chosen with equal probability.

    Parameters:
    - length (int): The number of steps in the random walk. Must be a non-negative integer. Default is 10000.
    - seed (int, optional): An optional seed value to initialize the random number generator. Use this for reproducible results.

    Requirements:
    - numpy
    - random

    Returns:
    - np.array: A numpy array representing the positions of the walk at each step. Starts at 0.

    Raises:
    - ValueError: If `length` is negative.

    Example:
    >>> random.seed(0)     # For reproducibility in doctest
    >>> walk = task_func(5)
    >>> walk.tolist()
    [0, 1, 2, 1, 0, 1]
    """
    if 0 > length:
        raise ValueError("length must be a non-negative integer")
    random.seed(seed)
    steps = [1 if 0.5 < random.random() else -1 for _ in range(length)]
    return np.cumsum([0] + steps)
