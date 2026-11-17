import pandas as pd
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    """
    Analyzes numerical data from a CSV file. The function reads the CSV file, converts string representations of
    numbers with commas into floating point numbers, calculates the mean and standard deviation for each numerical column,
    generates a histogram plot for each numerical column, and performs an ANOVA test to check the statistical significance 
    of differences between means of numerical columns (if applicable).

    Parameters:
    - data_file_path (str): Path to the CSV data file.

    Returns:
    - means (pd.Series): Mean values of each numerical column.
    - std_devs (pd.Series): Standard deviation values of each numerical column.
    - axes (list[matplotlib.axes.Axes]): List of histogram plots for each numerical column.
    - anova_results (pd.DataFrame): ANOVA test results for each pair of numerical columns (if more than one numerical column is present).

    Requirements:
    - pandas
    - sklearn

    Note:
    - The function assumes that all columns in the CSV file contain numerical data or string representations of numerical data.
    - The ANOVA test is only performed if there are two or more numerical columns. Compute two columns "F-value" and "P-value" for each pair of numerical columns.

    Example:
    >>> means, std_devs, axes, anova_results = task_func('data.csv')
    >>> print(f'Means: {means}, Standard Deviations: {std_devs}')
    >>> print(anova_results)
    """
    df = pd.read_csv(data_file_path)
    # Convert strings with commas to float, if applicable
    for col in df.columns:
        df[col] = pd.to_numeric(df[col].replace(",", "", regex=True), errors="coerce")
    # drop columns with NaN values
    df = df.dropna(axis=1)
    means = df.mean()
    std_devs = df.std()

    # Creating a histogram for each numerical column
    axes = []
    for col in df.columns:
        ax = df[col].hist(bins=50)
        ax.set_title(col)
        axes.append(ax)

    plt.show()

    # ANOVA Test if more than one numerical column
    anova_results = None
    if len(df.columns) > 1:
        anova_results = pd.DataFrame(f_oneway(*[df[col] for col in df.columns if df[col].dtype != 'object']),
                                     index=['F-value', 'P-value'], 
                                     columns=['ANOVA Results'])

    return means, std_devs, axes, anova_results
