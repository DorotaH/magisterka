from random import randint

import matplotlib.pyplot as plt
import numpy as np


def task_func(array_length=100):
	"""
	Generate two arrays of random integers and draw a line diagram with the
	maximum values of the respective elements of the two arrays. Set 'Maximum Values' on its y-axis.

	Parameters:
	- array_length (int): Length of the random arrays to be generated. Default is 100.

	Returns:
	- matplotlib.axes.Axes: Axes object with the plot.

	Requirements:
	- numpy
	- matplotlib.pyplot
	- random

	Example:
	>>> ax = task_func(100)
	"""
	array1 = np.array([randint(1, 100) for _ in range(array_length)])
	array2 = np.array([randint(1, 100) for _ in range(array_length)])

	max_values = np.maximum(array1, array2)

	fig, ax = plt.subplots()
	ax.plot(max_values)
	ax.set_ylabel("Maximum Values")

	return ax
