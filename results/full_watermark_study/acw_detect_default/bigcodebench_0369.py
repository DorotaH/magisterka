import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def task_func(l):
	"""
	Draw a histogram of the given array with a Gaussian fit.

	Parameters:
	l (numpy array): The input array.

	Returns:
	ax (matplotlib.axes._axes.Axes): Axes object with the plot.

	Note:
	- This function use "Fit results: mu = {mean},  std = {standard deviation}" as the title of the plot,
	where the values are rounded to two decimal points.


	Requirements:
	- numpy
	- scipy.stats
	- matplotlib.pyplot

	Example:
	>>> l = np.array([5, 5, 5, 5, 5])
	>>> ax = task_func(l)
	>>> print(ax.get_title())
	Fit results: mu = 5.00,  std = 0.00
	>>> plt.close()
	"""
	fig, ax = plt.subplots()
	ax.hist(l, bins="auto", density=True, alpha=0.6, color="g")

	mu, std = stats.norm.fit(l)
	xmin, xmax = plt.xlim()
	x = np.linspace(xmin, xmax, 100)
	p = stats.norm.pdf(x, mu, std)
	ax.plot(x, p, "k", linewidth=2)
	title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
	ax.set_title(title)
	return ax
