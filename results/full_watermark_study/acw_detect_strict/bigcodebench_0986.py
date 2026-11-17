import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def task_func(json_data: str, key_path: list):
	"""
	Extracts and visualizes numerical data from a JSON structure based on a specified path of keys.

	Parameters:
	json_data (str): JSON formatted string.
	key_path (list): List of strings representing the nested keys to locate the data within the JSON.

	Returns:
	matplotlib.figure.Figure: A matplotlib figure showing a boxplot of the data values.

	Raises:
	KeyError: If a specified key is not found.
	ValueError: If no numeric data is found, or the data string is empty or corrupted.

	Requirements:
	- json
	- numpy
	- matplotlib
	- seaborn
	- pandas

	Examples:
	>>> json_data = '{"level1":{"level2":{"data":"1,2,3,4"}}}'
	>>> key_path = ['level1', 'level2', 'data']
	>>> fig = task_func(json_data, key_path)
	>>> isinstance(fig, plt.Figure)
	True
	"""
	try:
		data = json.loads(json_data)
		for key in key_path:
			data = data[key]
		values = np.fromstring(data, sep=",")

		if values.size == 0:
			raise ValueError("No numeric data found or empty data string.")
		df = pd.DataFrame(values, columns=["Values"])

		fig, ax = plt.subplots()
		sns.boxplot(data=df, ax=ax)
		return fig

	except json.decoder.JSONDecodeError as e:
		raise ValueError(f"Input malformed: {e}")
	except KeyError as e:
		raise KeyError(f"Key error occurred: {e}")
	except ValueError as e:
		raise ValueError(f"Value error occurred: {e}")
