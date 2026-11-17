import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def task_func(range_start=-10, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples. Each tuple contains x, sin(x), and cos(x) 
    values. The function then plots the sine and cosine functions using these values along with the absolute 
    difference between the two functions and returns the plot. Finally, it returns the magnitude of the mean 
    and median of the 1D fft of the absolute difference between the two functions.

    Parameters:
    - range_start: The starting value of the x range.
    - range_end: The ending value of the x range.
    - step: The step size for the x values.

    Returns:
    tuple: A tuple containing two items:
        - generator: A generator object producing tuples in the format (x, sin(x), cos(x), abs(sin(x) - cos(x)).
        - ax: An Axes object representing the plot.
        - float: The abs of the mean of the 1D fft of the absolute difference between sin(x) and cos(x).
        - float: The abs of the median of the 1D fft of the absolute difference between sin(x) and cos(x).

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.fft

    Example:
    >>> data, ax, fft_mean, fft_median = task_func()
    >>> print(next(data))
    (-10.0, 0.5440211108893698, -0.8390715290764524, 1.383092639965822)
    """
    if range_start>range_end:
        raise ValueError("range_start cannot be smaller than range_end.")

    x_values = np.arange(range_start, range_end, step)
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    fft_values = fft([abs(np.sin(x) - np.cos(x)) for x in x_values])
    _, ax = plt.subplots()
    for x, sin_x, cos_x, abs_x in data:
        ax.scatter(x, sin_x, color='b')
        ax.scatter(x, cos_x, color='r')
        ax.scatter(x, abs_x, color='g')
    
    # We recreate the generator since it was exhausted in the for loop above
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    return data, ax, abs(np.mean(fft_values)), abs(np.median(fft_values))
