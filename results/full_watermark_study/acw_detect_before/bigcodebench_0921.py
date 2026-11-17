import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def task_func(data, columns):
	"""
	Normalizes specified columns of a DataFrame using min-max scaling.

	Parameters:
	data (dict): A dictionary where keys are column names and values are lists of values.
	columns (list of str): A list of column names to be normalized.

	Returns:
	pandas.DataFrame: A new DataFrame with the specified columns normalized between 0 and 1.

	Requirements:
	- pandas
	- sklearn.preprocessing

	Constants:
	- A MinMaxScaler object from sklearn.preprocessing is used internally for scaling.

	Example:
	>>> data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
	>>> normalized_df = task_func(data, ['a', 'b'])
	>>> print(normalized_df)
		a    b
	0  0.0  0.0
	1  0.5  0.5
	2  1.0  1.0
	"""
	df = pd.DataFrame(data)
	# Create a local MinMaxScaler object
	scaler = MinMaxScaler()
	
	# Create a copy of the DataFrame to avoid modifying the original DataFrame
	df_copy = df.copy()

	# Normalize the specified columns
	df_copy[columns] = scaler.fit_transform(df_copy[columns])

	return df_copy
