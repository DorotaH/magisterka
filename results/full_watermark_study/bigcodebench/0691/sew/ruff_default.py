import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def task_func(df):
    """
    Given a pandas DataFrame with random numeric values, run KMeans clusters on the data and return the labels.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - labels (np.array): The labels from the KMeans clustering.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.rand(500, 2) * 100, columns=['A', 'B'])
    >>> labels = task_func(df)
    >>> print(labels)
    [0 2 1 0 2 0 2 1 0 1 1 1 0 0 1 1 0 2 1 2 0 0 0 0 1 2 2 2 1 1 1 2 0 0 0 1 0
     2 1 1 2 1 1 2 2 0 2 2 1 1 0 0 2 0 1 1 2 2 1 2 2 1 1 2 0 1 1 2 2 0 2 1 1 2
     1 2 0 2 2 0 0 2 0 1 0 1 1 1 2 2 1 2 0 2 1 0 2 1 2 2 1 0 1 0 1 2 1 1 0 2 2
     1 1 2 2 2 2 0 1 1 2 2 0 0 2 1 2 0 2 1 2 0 2 2 1 2 2 2 2 2 2 1 1 0 0 1 2 0
     1 1 0 2 2 1 2 1 0 2 1 1 2 1 2 2 1 0 1 1 2 1 1 1 0 1 0 0 1 0 0 2 0 0 2 2 1
     1 0 1 1 2 0 2 2 1 2 2 0 0 2 2 0 0 0 1 1 0 2 2 1 2 2 0 0 0 1 0 1 0 0 1 0 1
     2 2 1 2 0 0 0 1 0 2 2 0 0 0 0 0 0 2 2 0 2 1 2 0 1 1 1 2 2 0 1 2 2 2 2 1 0
     2 1 2 2 1 0 2 2 2 2 1 2 0 1 0 0 0 2 2 1 2 1 1 0 1 2 0 0 2 0 1 0 1 1 1 1 0
     1 2 1 1 1 1 0 1 0 0 1 2 1 2 1 1 1 0 1 2 2 0 1 1 1 1 0 2 2 0 2 1 1 2 0 1 1
     1 1 0 0 0 1 2 2 0 2 1 1 1 1 0 0 0 1 1 0 0 0 2 1 0 2 0 2 0 2 0 1 0 2 0 0 1
     1 2 0 0 2 0 1 0 2 2 1 0 0 2 0 0 1 1 0 2 2 1 0 1 0 0 2 0 2 2 1 2 0 2 1 2 0
     2 1 1 1 1 0 1 2 1 1 1 2 2 0 0 1 0 2 0 0 1 0 1 2 1 0 1 2 1 2 1 2 1 0 1 1 1
     1 2 2 1 0 1 1 0 0 2 1 1 2 1 0 1 2 2 1 0 1 0 2 1 0 0 0 2 1 0 2 2 0 1 1 0 0
     1 1 2 2 2 1 1 1 2 0 1 2 2 0 2 0 1 2 2]
    """
    # Perform clustering
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df.values)

    # Convert standardized values back to a DataFrame using pd
    df_std = pd.DataFrame(df_std, columns=df.columns)

    # Perform clustering with sklearn's KMeans
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_std)
    labels = kmeans.labels_  # The labels are directly a numpy array

    return labels
