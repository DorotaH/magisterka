import sqlite3

import pandas as pd


def task_func(db_name, table_name):
    """
    Plot the relationship between the first and second numerical columns of an SQLite3 table, after excluding 'id' column.

    Parameters:
    - db_name (str): The absolute path to the SQLite3 database.
    - table_name (str): The name of the table to plot from.

    Returns:
    - matplotlib.axes._axes.Axes: Scatterplot with column name labeled on their respective axes.

    Raises:
    - ValueError: If the table has less than two numerical columns.

    Requirements:
    - sqlite3
    - pandas

    Example:
    >>> ax = task_func('/path/to/database/test.db', 'People')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.9400000000000001, 0, '0.94'), ... ]
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Dynamically get the first two numerical columns from the table (excluding 'id')
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if "id" in numerical_columns:
        numerical_columns.remove("id")
    if len(numerical_columns) < 2:
        raise ValueError("The table must have at least two numerical columns to plot.")

    return df.plot.scatter(x=numerical_columns[0], y=numerical_columns[1])
