import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)


def task_func(L):
	'''
	Generates a DataFrame filled with random integers. The dimensions of the DataFrame (number of rows and columns)
	are determined by multiplying pairs of integers from nested lists within the input list of lists 'L'.
	
	Requirements:
	- numpy
	- pandas

	Parameters:
	L (list of lists): A list of lists where each sublist contains two integers.
	
	Returns:
	DataFrame: A pandas DataFrame with random integers.
	
	Example:
	>>> df = task_func([[2, 3], [5, 6]])
	>>> type(df)
	<class 'pandas.core.frame.DataFrame'>
	'''
	rows, columns = L[0][0] * L[0][1], L[1][1] * L[1][0]
	random_array = np.random.randint(RANGE[0], RANGE[1], size=(rows, columns))
	return pd.DataFrame(random_array)
