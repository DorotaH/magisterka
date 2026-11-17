from collections import Counter

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def task_func(df, n_clusters=3, random_state=None, n_init=10):
    """
	Identify duplicate points in a DataFrame, perform KMeans clustering on the unique points,
	and record the clusters.

	Parameters:
	df (pd.DataFrame): A DataFrame containing at least two columns 'x' and 'y' representing points.
	n_clusters (int, optional): Number of clusters for KMeans clustering. Default is 3.
	random_state (int, optional): The seed used by the random number generator for reproducibility. Default is None.
	n_init (int, optional): Number of time the k-means algorithm will be run with different centroid seeds.
							The final results will be the best output of n_init consecutive runs in terms of
							within-cluster sum of squares. Default is 10.

	Returns:
	tuple: A tuple containing:
		- Counter: A Counter object with the count of duplicate points.
		- pd.DataFrame: A DataFrame with an additional column 'cluster' representing cluster assignments for unique points.
		- Axes: A scatter plot of the clustered data.

	Requirements:
	- collections.Counter
	- sklearn.cluster.KMeans
	- matplotlib.pyplot

	Example:
	>>> df = pd.DataFrame({\
			'x': [1, 2, 2, 2, 3, 4],\
			'y': [1, 1, 1, 1, 3, 3]\
		})
	>>> duplicates, df_clustered, ax = task_func(df, random_state=42)
	>>> df_clustered
	x  y  cluster
	0  1  1        2
	1  2  1        0
	4  3  3        1
	5  4  3        1
	>>> duplicates
	Counter({(2, 1): 3})
	"""
    # Identify duplicates
    duplicates = df[df.duplicated(subset=["x", "y"], keep=False)]
    duplicates_counter = Counter(map(tuple, duplicates[["x", "y"]].values))

    # Remove duplicates and perform KMeans clustering on unique points
    unique_df = df.drop_duplicates(subset=["x", "y"]).copy()

    # Adjust n_clusters if unique data points are fewer than desired clusters
    n_clusters = min(n_clusters, len(unique_df))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_df["cluster"] = kmeans.fit_predict(unique_df[["x", "y"]])

    # Plot clustered data
    fig, ax = plt.subplots()
    scatter = ax.scatter(unique_df["x"], unique_df["y"], c=unique_df["cluster"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("KMeans Clusters")

    return duplicates_counter, unique_df, ax
