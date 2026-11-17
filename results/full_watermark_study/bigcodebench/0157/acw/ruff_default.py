import pandas as pd
import seaborn as sns


def task_func(data):
    """
    Analyze a dataset by calculating the average of values across each row and visualizing the correlation matrix as a
    heatmap.

    Parameters:
    data (numpy.array): 2D array where each row represents a record and each column represents a feature

    Returns:
    tuple: A tuple containing:
            - DataFrame: A pandas DataFrame enhanced with an 'Average' column that represents the mean across each row.
            - Axes: The matplotlib Axes object showing the heatmap of the correlations.

    Requirements:
    - pandas
    - numpy
    - seaborn

    Raises:
    ValueError: If the input data is not a 2D array or if it contains non-numeric data.

    Example:
    >>> data = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]])
    >>> df, ax = task_func(data)
    >>> print(df['Average'].to_string(index=False))
    4.5
    4.5
    """

    if not isinstance(data, np.ndarray) or data.ndim != 2:
        raise ValueError("Input data must be a 2D numpy array.")

    df = pd.DataFrame(data)

    # Calculate correlation matrix
    correlation = df.corr()
    # Plot the heatmap
    ax = sns.heatmap(correlation, annot=True, cmap="coolwarm")

    # Compute the average for each row and add it as a new column
    df["Average"] = df.mean(axis=1)

    return df, ax
