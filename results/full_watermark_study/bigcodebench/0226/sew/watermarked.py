import  numpy as  np
import  math
import  matplotlib.pyplot as  plt

def task_func(range_start=0, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains x and e^x values. Plot the exponential function using these values.

    Returns:
    tuple: 
        - A generator object that yields tuples of (x, e^x).
        - The plotted Axes object of the exponential function.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot

    Example:
    >>> data, ax = task_func()
    >>> print(next(data))
    (0.0, 1.0)
    >>> ax.get_title()  # Returns the title of the plot
    'Exponential Function Plot'
    """
    x_values = np.arange(range_start, range_end, step)
    data = ((x, math.exp(x)) for  x in  x_values)
    _, ax = plt.subplots()
    for  x, exp_x in  data:
        ax.scatter(x, exp_x, color='b')
    ax.set_title("Exponential Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("e^x")
    data = ((x, math.exp(x)) for  x in  x_values)
    return  data, ax
