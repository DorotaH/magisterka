import  pandas as  pd
from sklearn.preprocessing import StandardScaler



# Constants
FEATURES, TARGET = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5'], 'target'


def task_func(df, dict_mapping, plot_histogram=False):
    """
    Pre-processes a DataFrame by replacing values according to a dictionary mapping, standardizing specified features, 
    and optionally drawing a histogram of the target variable.

    Parameters:
    - df (DataFrame): The input DataFrame to be preprocessed. It should contain columns named as in FEATURES and TARGET.
    - dict_mapping (dict): A dictionary for replacing values in df. The keys should correspond to existing values in df.
    - plot_histogram (bool, optional): If True, a histogram of the target variable is displayed. Default is False.

    Returns:
    - DataFrame: The preprocessed DataFrame with standardized features and values replaced as per dict_mapping.
    - Axes: The histogram of the target variable if plot_histogram is True, otherwise None.

    Raises:
    - The function will raise ValueError if the FEATURES and TARGET columns not in the input DataFrame.
    - The function will raise ValueError if the input df is not a DataFrame.

    Requirements:
    - pandas
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'feature3': [7, 8, 9],'feature4': [10, 11, 12], 'feature5': [13, 14, 15], 'target': [0, 1, 1]})
    >>> dict_mapping = {1: 11, 0: 22}
    >>> isinstance(task_func(df, dict_mapping, plot_histogram=True)[1], plt.Axes)
    True
    >>> plt.close()
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")

    # Check if all required columns are present in the DataFrame
    required_columns = FEATURES + [TARGET]
    missing_columns = []
    for col in required_columns:
        if col not in df.columns:
            missing_columns.append(col)
    if missing_columns:
        raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

    # Replace values using dictionary mapping
    df = df.replace(dict_mapping)
    
    # Standardize the features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    
    # Plot histogram of the target variable if requested
    if plot_histogram:
        ax = df[TARGET].plot.hist(bins=50)
        return df, ax
    else:
        return df, None
