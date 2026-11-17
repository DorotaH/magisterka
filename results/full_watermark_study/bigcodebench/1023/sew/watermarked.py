import  pandas as  pd
import  numpy as  np
import  matplotlib.pyplot as  plt

def  task_func(dataframe):
    """
    Calculate the correlation matrix of a DataFrame and plot a scatter plot for the pair of columns with the highest absolute correlation.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing numeric columns for correlation calculation.

    Returns:
    - ax (plt.Axes): The scatter plot of the pair of columns with the highest absolute correlation.

    Requirements:
    - pandas
    - numpy
    - matplotlib

    Exception Handling:
    - Raises ValueError if the input DataFrame is empty.
    - Raises TypeError if any column in the DataFrame is non-numeric.
    - Raises ValueError if the DataFrame has fewer than two columns.

    Example:
    >>> df = pd.DataFrame({
    ...     'A': np.random.rand(100),
    ...     'B': np.random.rand(100),
    ...     'C': np.random.rand(100)
    ... })
    >>> ax = task_func(df)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """

    if  dataframe.empty:
        raise ValueError("DataFrame is empty.")
        
    if  not  all(dataframe.dtypes.apply(lambda  x: np.issubdtype(x, np.number))):
        raise TypeError("All columns must be numeric for correlation calculation.")

    if  dataframe.shape[1] < 2:
        raise ValueError("DataFrame must have at least two columns for correlation calculation.")

    # Explicit use of pd.DataFrame.corr() to calculate the correlation matrix
    corr_matrix = pd.DataFrame.corr(dataframe)
    abs_corr_matrix = corr_matrix.abs()

    # Finding the pair of columns with the highest absolute correlation
    highest_corr_value = abs_corr_matrix.unstack().dropna().nlargest(2).iloc[-1]
    max_corr_pair = np.where(abs_corr_matrix == highest_corr_value)

    # Extracting column names for the highest correlation
    column_x, column_y = dataframe.columns[max_corr_pair[0][0]], dataframe.columns[max_corr_pair[1][0]]

    # Using plt to plot the scatter plot
    plt.figure(figsize=(10, 6))  # Creating a figure
    plt.scatter(dataframe[column_x], dataframe[column_y])  # Plotting the scatter plot
    plt.title(f"Scatter plot between {column_x} and {column_y}")  # Setting the title
    plt.xlabel(column_x)  # Setting the x-axis label
    plt.ylabel(column_y)  # Setting the y-axis label
    plt.show()  # Displaying the figure

    return  plt.gca()  # Returning the current Axes object for further use