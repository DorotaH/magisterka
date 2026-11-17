import itertools

import matplotlib.pyplot as plt
import seaborn as sns

# Constants
SHAPES, COLORS = (
    [
        "Circle",
        "Square",
        "Triangle",
        "Rectangle",
        "Pentagon",
        "Hexagon",
        "Heptagon",
        "Octagon",
        "Nonagon",
        "Decagon",
    ],
    [
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Black",
        "White",
        "Purple",
        "Orange",
        "Pink",
        "Brown",
    ],
)


def task_func(num_pairs=10):
    """
    Generate and display a countplot of predefined shape-color pairs.

    This function creates a visual representation of a specified number of unique shape-color combinations,
    each displayed as a bar in the countplot. The shape-color pairs are selected from a predefined list.

    Parameters:
    - num_pairs (int): The number of unique shape-color pairs to be displayed in the countplot.
                       Default is 10. If the requested number is less than 1 or greater than the total
                       possible unique combinations (100), it is adjusted to the valid range (1 to 100).

    Returns:
    - ax (matplotlib.axes._axes.Axes): The Axes object of the countplot, which can be used for
                                                  further customizations or to retrieve information about the plot.

    Requirements:
    - itertools
    - seaborn
    - matplotlib

    Example:
    >>> ax = task_func(10)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(9)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(8)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(7)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(6)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    """
    max_pairs = len(SHAPES) * len(COLORS)
    num_pairs = min(num_pairs, max_pairs)

    pairs = [f"{s}:{c}" for s, c in itertools.product(SHAPES, COLORS)][0:num_pairs]

    # Drawing the countplot
    ax = sns.countplot(x=pairs, hue=pairs, palette="Set3", legend=False)
    plt.xticks(rotation=90)

    return ax
