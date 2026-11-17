import pandas as pd
import time
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')


def task_func(data, letter):
	"""
	Filters rows in a dictionary where the 'Name' column values start with a specified letter.
	First, convert the dict to a DataFrame and then filter rows in this DataFrame.

	Parameters:
	- df (dic of list): The input dict. It should have a 'Name' key.
	- letter (str): The letter to filter the 'Name' column by.

	Returns:
	- pd.Series: A Series of filtered 'Name' column.

	Requirements:
	- pandas
	- time

	Example:
	>>> data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Fiona']}
	>>> filtered_names = task_func(data, 'a')
	>>> filtered_names.index[0].startswith('A')
	True
	>>> len(filtered_names)
	1
	"""
	df = pd.DataFrame(data)
	start_time = time.time()
	regex = f'^{letter}'
	filtered_df = df[df['Name'].str.contains(regex, case=False, regex=True)]
	end_time = time.time()  # End timing
	cost = f"Operation completed in {end_time - start_time} seconds."
	return filtered_df['Name'].value_counts()
