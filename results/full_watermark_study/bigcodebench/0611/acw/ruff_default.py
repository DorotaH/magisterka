from random import sample

import matplotlib.pyplot as plt

# Constants
COLUMNS = ["A", "B", "C", "D", "E"]


def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns,
    and then create n random line plots of two columns against each other.

    Parameters:
    - df (pd.DataFrame): The input pandas DataFrame.
    - tuples (list of tuple): A list of tuples, each tuple represents values in a row to be removed.
    - n_plots (int): The number of line plots to generate.

    Returns:
    - (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
    Each entry in the plot details list is a tuple containing the two columns plotted against each other.

    Requirements:
    - matplotlib.pyplot
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plot_details = task_func(df, tuples, 3)
    """
    mask = df.apply(tuple, axis=1).isin(tuples)
    df = df[~mask]

    plot_details = []
    for _ in range(min(n_plots, len(df))):
        selected_columns = sample(COLUMNS, 2)
        df.plot(x=selected_columns[0], y=selected_columns[1], kind="line")
        plot_details.append((selected_columns[0], selected_columns[1]))

    plt.show()

    return df, plot_details
