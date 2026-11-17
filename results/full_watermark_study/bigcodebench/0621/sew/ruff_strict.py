from itertools import chain

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler


def task_func(L):
    """
    Convert a list of lists 'L' into a single list of integers, standardize the integers, and plot the standardized values.

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.

    Returns:
    matplotlib.axes._axes.Axes: A plot displaying the standardized values.

    Requirements:
    - numpy
    - itertools
    - sklearn.preprocessing
    - matplotlib.pyplot

    Examples:
    >>> ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    """
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    fig, ax = plt.subplots()
    ax.plot(standardized_data)
    plt.close(fig)
    return ax
