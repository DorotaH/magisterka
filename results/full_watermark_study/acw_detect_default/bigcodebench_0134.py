import matplotlib.pyplot as plt
import pandas as pd


def task_func(df, bins=20):
	"""
	Draw a histogram of the last column of the DataFrame and return the plot.

	Parameters:
	- df (DataFrame): The input DataFrame, which must contain at least one column.
	- bins (int, optional): Number of bins for the histogram. Defaults to 20.

	Returns:
	- Axes: A Matplotlib Axes object representing the histogram of the last column. The histogram includes:
	- Title: 'Histogram of ' followed by the name of the last column.
	- X-axis label: 'Value'
	- Y-axis label: 'Frequency'

	Raises:
	- ValueError: If the input is not a DataFrame, or if the DataFrame is empty.

	Requirements:
	- pandas
	- matplotlib.pyplot

	Example:
	>>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
	>>> ax = task_func(df)
	>>> plt.show()
	"""

	if not isinstance(df, pd.DataFrame) or df.empty:
		raise ValueError("The input must be a non-empty pandas DataFrame.")

	last_col_name = df.columns[-1]
	fig, ax = plt.subplots()
	ax.hist(df[last_col_name], bins=bins)
	ax.set_title(f"Histogram of {last_col_name}")
	ax.set_xlabel("Value")
	ax.set_ylabel("Frequency")
	plt.show()
	return ax
