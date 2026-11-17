import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler


def task_func(x, y, labels):
	"""
	Scale the "x" and "y" arrays using the standard scaler of sklearn and plot them with given labels.
	Each pair of x and y arrays are scaled independently and plotted as a separate series with a label.

	Parameters:
	- x (list of np.ndarray): List of numpy arrays representing the x-values of the data points.
	- y (list of np.ndarray): List of numpy arrays representing the y-values of the data points.
	- labels (list of str): List of strings representing the labels for each data series.

	Returns:
	- matplotlib.figure.Figure: The figure object containing the plot.

	Requirements:
	- numpy
	- matplotlib.pyplot
	- sklearn.preprocessing

	Example:
	>>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
	>>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
	>>> labels = ['A', 'B', 'C']
	>>> fig = task_func(x, y, labels)
	>>> plt.show()
	"""
	scaler = StandardScaler()

	fig, ax = plt.subplots()

	# Iterate over the datasets, scale each, and plot
	for i in range(len(x)):
		# Combine x and y values and scale them
		xy = np.vstack((x[i], y[i])).T  # Transpose to get correct shape for scaling
		xy_scaled = scaler.fit_transform(xy)  # Scale data

		# Plot scaled data
		ax.plot(xy_scaled[:, 0], xy_scaled[:, 1], label=labels[i])

	ax.legend()  # Add a legend to the plot

	return fig  # Return the figure object containing the plot
