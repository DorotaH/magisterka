import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
	'''
	Create a histogram of a normal distribution with a given mean and standard deviation, and overlay the 
	probability density function (PDF) of the normal distribution on the histogram. Additionally, overlay a 
	second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) 
	regression. The random seed is set for reproducibility. The color of the PDF line is red, and the color of the OLS line is green.
	
	Parameters:
	- mu (float): The mean of the distribution.
	- sigma (float): The standard deviation of the distribution.
	- seed (int, Optional): The random seed for reproducibility. Defaults to 0.
	- num_samples (int, Optional): The number of samples to generate from the distribution. Defaults to 1000.
	- num_bins (int, Optional): The number of bins to use in the histogram. Defaults to 30.
	
	Returns:
	- matplotlib.axes.Axes: The Axes object with the histogram and overlaid PDF.
	
	Requirements:
	- numpy
	- matplotlib.pyplot
	- statsmodels.formula.api
	
	Example:
	>>> ax = task_func(0, 1)
	>>> type(ax)
	<class 'matplotlib.axes._axes.Axes'>
	'''
	np.random.seed(seed)
	samples = np.random.normal(mu, sigma, num_samples)

	# Create a histogram and get the Axes object
	fig, ax = plt.subplots()
	count, bins, ignored = ax.hist(samples, num_bins, density=True)
	ax.plot(
		bins, 
		1 / (sigma * np.sqrt(2 * np.pi)) * \
		np.exp( - (bins - mu)**2 / (sigma**2 * 2) ), linewidth=2, color='r'
	)
	bins = (bins[:-1] + bins[1:]) / 2
	model = ols('count ~ bins + np.power(bins, 2)', data={'count': count, 'bins': bins}).fit()
	ax.plot(
		bins, 
		model.params['Intercept'] + bins * model.params['bins'] + \
		model.params['np.power(bins, 2)'] * np.power(bins, 2), linewidth=2, color='g'
	)
	
	return ax
