from random import randint

import matplotlib.pyplot as plt
import pandas as pd


def task_func(num_rows=5, rand_range=(0, 100)):
    """
    Create a DataFrame containing random integer values within a specified range for categories 'A' through 'E',
    and visualize this data with a stacked bar chart.

    Parameters:
    num_rows (int): Specifies the number of rows in the DataFrame.
    rand_range (tuple): Defines the lower and upper bounds for the random number generation, inclusive.

    Returns:
    matplotlib.figure.Figure: The matplotlib Figure object containing the plotted data.

    Requirements:
    - pandas
    - matplotlib
    - random

    Example:
    >>> fig = task_func(num_rows=3, rand_range=(10, 50))
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """
    labels = ["A", "B", "C", "D", "E"]
    data = pd.DataFrame(
        {
            label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]
            for label in labels
        }
    )

    fig, ax = plt.subplots()

    data.plot(kind="bar", stacked=True, ax=ax)

    return fig
