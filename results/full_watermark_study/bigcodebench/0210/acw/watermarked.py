import collections
from operator import itemgetter
import matplotlib.pyplot as plt


def task_func(data):
	"""
	Generate a bar plot showing the frequency of letters in the given dataset, 
	and highlight the letter associated with the maximum integer value.
	
	Parameters:
	data (list of tuples): A list where each tuple contains a letter (str) and an integer.

	Returns:
	matplotlib.axes.Axes: The Axes object of the generated plot, with the x-axis labeled 'Letter', the y-axis labeled 'Count', the title 'Letter Counts with Max Value Letter Highlighted', and the labels 'Letter Counts' and 'Max Value Letter' in the legend.
	
	Requirements:
	- collections
	- operator
	- matplotlib.pyplot

	Example:
	>>> dataset = [('a', 10), ('b', 15), ('a', 5), ('c', 20)]
	>>> ax = task_func(dataset)
	>>> type(ax)
	<class 'matplotlib.axes._axes.Axes'>
	"""
	letter_counts = collections.Counter([item[0] for item in data])
	max_value_letter = max(data, key=itemgetter(1))[0]

	letters, counts = zip(*letter_counts.items())
	# Initialize a fresh plot
	plt.figure()
	ax = plt.bar(letters, counts, label='Letter Counts')

	if max_value_letter in letter_counts:
		plt.bar(max_value_letter, letter_counts[max_value_letter], color='red', label='Max Value Letter')

	plt.xlabel('Letter')
	plt.ylabel('Count')
	plt.title('Letter Counts with Max Value Letter Highlighted')
	plt.legend()

	return plt.gca()
