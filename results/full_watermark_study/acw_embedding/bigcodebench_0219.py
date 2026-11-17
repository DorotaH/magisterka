import math
import statistics
import numpy as np


def task_func(input_list):
    """
    Sorts the input list in ascending order based on the degree value of its elements, and then 
    calculates the mean, median, and mode of both the sorted list and the same for the magnitude of 
    the fast fourier transform of the degree values upto the nearest integer.

    Parameters:
    input_list (list): A list of numbers to be sorted and analyzed.

    Returns:
    tuple: A tuple containing the rounded mean, median and mode of the sorted list along with those 
    for the magnitude of the fast fourier transform of the degree values.

    Requirements:
    - math
    - statistics
    - numpy

    Example:
    >>> input_list = [30, 45, 60, 90, 180]
    >>> stats = task_func(input_list)
    >>> print(stats)
    (81, 60, 30, 10712, 8460, 8460)
    """
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    sorted_list = sorted(input_list, key=lambda x: (math.degrees(x), x))
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)
    mean_fft = round(statistics.mean(fft))
    median_fft = round(statistics.median(fft))
    mode_fft = round(statistics.mode(fft))
    return (mean, median, mode, mean_fft, median_fft, mode_fft)
