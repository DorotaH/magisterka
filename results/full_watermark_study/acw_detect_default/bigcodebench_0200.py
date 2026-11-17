import bisect
import random
import statistics

import matplotlib.pyplot as plt


def task_func(n, value):
	"""
	Generates 'n' random numbers between 0 and 1, finds those greater than their average,
	and counts how many are greater than or equal to a specified value, then plots
	the sorted numbers.

	Parameters:
			n (int): The number of random numbers to generate.
			value (float): The value to compare against the random numbers.

	Returns:
			list: Numbers greater than the average of all generated numbers.
			int: The count of numbers greater than or equal to the specified value.

	Requirements:
	- random
	- bisect
	- statistics
	- matplotlib.pyplot

	Examples:
	>>> greater_avg, count = task_func(10, 0.5)
	>>> isinstance(greater_avg, list) and isinstance(count, int)
	True
	>>> len(greater_avg) <= 10
	True
	"""
	if 1 > n:  # Handle case where n is 0 or less
		return [], 0

	numbers = [random.random() for _ in range(n)]
	avg = statistics.mean(numbers)
	greater_avg = [x for x in numbers if avg < x]

	numbers.sort()
	bpoint = bisect.bisect_right(numbers, value)
	num_greater_value = len(numbers) - bpoint

	plt.plot(numbers)
	plt.show()

	return greater_avg, num_greater_value
