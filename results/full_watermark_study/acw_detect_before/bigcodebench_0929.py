import numpy as np
from scipy import stats


def task_func(word: str) -> np.ndarray:
	"""
	Calculate the difference between the ASCII values of each pair of adjacent letters in the input word.
	After calculating the difference, calculate the entropy of the differences.
	
	Requirements:
	- numpy
	- scipy.stats
	
	Parameters:
	- word (str): The input word as a string.
	
	Returns:
	- np.ndarray: A numpy array containing the difference between the ASCII values of each pair of adjacent letters in the word.
	- float: The entropy of the differences.
	
	Examples:
	>>> task_func('abcdef')
	(array([1, 1, 1, 1, 1]), 1.6094379124341005)
	>>> task_func('hello')
	(array([-3,  7,  0,  3]), -inf)
	"""
	if not word:  # Handling the case for empty string
		return np.array([])
	word_ascii_values = np.array([ord(x) for x in word])
	difference = np.diff(word_ascii_values)
	entropy = stats.entropy(difference)
	
	return difference, entropy
