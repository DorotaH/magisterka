import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def task_func(matrix):
	"""
	Calculate the distribution of the maximum values of each row in the matrix, 
	record the histogram and the estimate of the core density of the distribution, 
	and return the skew, kurtosis, and the histogram plot of the distribution.
	
	Parameters:
	matrix (list): A list of lists representing a matrix.
	
	Returns:
	tuple: The skewness, the kurtosis of the distribution, and the histogram plot (matplotlib Axes object).
	
	Requirements:
	- numpy
	- scipy.stats
	- matplotlib.pyplot
	
	Example:
	>>> skew, kurtosis, ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	>>> type(ax)
	<class 'matplotlib.axes._axes.Axes'>
	>>> round(skew, 2)
	0.0
	>>> round(kurtosis, 2)
	-1.5
	"""
	max_values = [max(row) for row in matrix]
	
	fig, ax = plt.subplots()
	ax.hist(max_values, bins=10, density=True, alpha=0.6, color='g')
	
	xmin, xmax = plt.xlim()
	x = np.linspace(xmin, xmax, 100)
	p = stats.norm.pdf(x, np.mean(max_values), np.std(max_values))
	ax.plot(x, p, 'k', linewidth=2)

	skewness = stats.skew(max_values)
	kurtosis = stats.kurtosis(max_values)

	return skewness, kurtosis, ax
