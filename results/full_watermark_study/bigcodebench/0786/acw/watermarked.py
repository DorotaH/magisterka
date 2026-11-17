import pandas as pd
import csv
import random


def task_func(
	n, 
	countries=['USA', 'UK', 'China', 'India', 'Germany'], 
	products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
	output_path=None,
	random_seed=None):
	"""
	Generate random sales data and return it as a pandas DataFrame.
	The sales data has the columns 'Country', 'Product' and 'Sales'.
	Country and Product get sampled from the provided lists / the default values.
	Sales is populated by generating random integers between 1 and 100.
	If an output_path is provided, the generated data is saved to a csv file.

	Parameters:
	n (int): The number of sales records to generate.
	countries (list, optional): List of countries for sales data generation. Defaults to ['USA', 'UK', 'China', 'India', 'Germany'].
	products (list, optional): List of products for sales data generation. Defaults to ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'].
	output_path (str, optional): Path to save the generated sales data as a CSV file. If not provided, the data will not be saved to a file.
	random_seed (int): Seed for rng. Used in generating the sales data. 

	Returns:
	DataFrame: A pandas DataFrame with the generated sales data.

	Requirements:
	- pandas
	- csv
	- random

	Example:
	>>> df = task_func(5, random_seed=1)
	>>> print(df)
	Country    Product  Sales
	0      UK  Product E     98
	1     USA  Product C     16
	2   India  Product D     61
	3   India  Product B     13
	4   India  Product A     50

	>>> df = task_func(7, products=['tea', 'coffee'], countries=['Austria', 'Australia'], random_seed=12)
	>>> print(df)
		Country Product  Sales
	0  Australia  coffee     85
	1  Australia     tea     49
	2    Austria  coffee     62
	3  Australia  coffee     89
	4    Austria     tea     85
	5    Austria  coffee     48
	6    Austria  coffee     27
	"""
	
	random.seed(random_seed)
	
	sales_data = []
	
	for _ in range(n):
		country = random.choice(countries)
		product = random.choice(products)
		sales = random.randint(1, 100)
		sales_data.append({'Country': country, 'Product': product, 'Sales': sales})

	# If an output path is provided, save the data to a CSV file
	if output_path:
		with open(output_path, 'w', newline='') as csvfile:
			fieldnames = ['Country', 'Product', 'Sales']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(sales_data)
		
	return pd.DataFrame(sales_data)
