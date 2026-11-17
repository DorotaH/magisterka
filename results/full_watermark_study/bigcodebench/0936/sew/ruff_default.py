import string

import matplotlib.pyplot as plt
import numpy as np

# Constants
ALPHABET = list(string.ascii_lowercase)


def task_func(word):
    """
    Draws a bar chart representing the positions of each letter in the given word
    within the English alphabet using numpy and matplotlib.pyplot.

    Parameters:
    word (str): The word whose letters' positions will be plotted.
                Should contain only lowercase alphabetic characters.

    Returns:
    Axes: A matplotlib.axes._axes.Axes object representing the generated plot.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Constants:
    - ALPHABET: A list containing all lowercase letters of the English alphabet.

    Examples:
    >>> ax = task_func('abc')
    >>> ax = task_func('hello')

    Note:
    The function uses the index of each letter in the English alphabet to represent its position.
    For example, 'a' will be represented by 1, 'b' by 2, and so on.
    """
    # Validate the input word to contain only alphabetic characters
    if not all(char in ALPHABET for char in word):
        raise ValueError(
            "The word should contain only lowercase alphabetic characters."
        )

    # Calculate the positions of each letter in the word within the alphabet
    letter_positions = np.array(list(map(lambda x: ALPHABET.index(x) + 1, word)))

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Draw the bar chart on the axis
    ax.bar(np.arange(len(letter_positions)), letter_positions)

    # Configure plot settings
    ax.set_xlabel("Letter Index")
    ax.set_ylabel("Alphabetical Position")
    ax.set_title("Alphabetical Position of Letters in Word")

    plt.show()

    return ax
