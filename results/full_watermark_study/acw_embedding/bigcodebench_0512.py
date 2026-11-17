import pandas as pd
import numpy as np


def task_func(column, data):
    """
    Analyze a list of sales data, calculate the sum, the mean, the minimum, the maximum of a given column,
    and return the bar chart plot for the given column without displaying it.

    Parameters:
    column (str): The column to analyze. Expected values are ['Product', 'Quantity Sold', 'Total Sales'].
    data (list): The sales data. Expected format: [['Product Name', Quantity Sold (int), Total Sales (int)], ...]
                 The function checks for data validity in the quantity columns (must not be negative).

    Returns:
    tuple: A tuple containing:
        - dict: A dictionary with the sum, mean, min, max of the column.
        - matplotlib.axes.Axes: The Axes object of the plotted bar chart. The bar chart will have Product in its
                                x-axis and the title Bar Chart of (column).

    Requirements:
    - pandas
    - numpy

    Raises:
    - ValueError: If the quantity sold or total sales is negative.
    
    Example:
    >>> data = [['Product A', 100, 10000], ['Product B', 150, 15000], ['Product C', 200, 20000]]
    >>> stats, plot = task_func('Total Sales', data)
    >>> stats
    {'sum': 45000, 'mean': 15000.0, 'min': 10000, 'max': 20000}
    >>> plot
    <Axes: title={'center': 'Bar Chart of Total Sales'}, xlabel='Product'>
    """
    COLUMNS = ["Product", "Quantity Sold", "Total Sales"]
    df = pd.DataFrame(data, columns=COLUMNS)
    if (df["Quantity Sold"] < 0).any() or (df["Total Sales"] < 0).any():
        raise ValueError("Value must not be negative")
    column_data = df[column]

    result = {
        "sum": np.sum(column_data),
        "mean": np.mean(column_data),
        "min": np.min(column_data),
        "max": np.max(column_data),
    }

    ax = df.plot.bar(x="Product", y=column, title=f"Bar Chart of {column}")

    return result, ax
