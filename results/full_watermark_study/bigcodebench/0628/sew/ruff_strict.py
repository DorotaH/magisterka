import math
from random import randint

import matplotlib.pyplot as plt


def task_func():
    """
    Create and draw a sine wave with random frequency, amplitude and phase shift. The return ax object
    has 'Random Sine Wave' title, 'Time' on the x axis and 'Amplitude' on the y axis.

    Parameters:
    None

    Returns:
    ax (matplotlib.axes._axes.Axes): The axis object of the generated sine wave plot.

    Requirements:
    - math
    - random
    - matplotlib.pyplot

    Example:
    >>> ax = task_func()
    """
    x, frequency = [i / 100 for i in range(1000)], randint(1, 5)
    amplitude, phase_shift = randint(1, 5), randint(0, 360)

    y = []
    for xi in x:
        y.append(amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)))

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Random Sine Wave")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.grid(True)

    return ax  # Return the axis object for testing
