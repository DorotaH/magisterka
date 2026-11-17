import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]


def task_func(file_path, save_path=None):
	"""
	This function processes a text dataset from a CSV file, performs text vectorization while excluding specific
	stopwords, and creates a histogram of the ten most common words. The function is robust to different input
	scenarios, such as empty data or data containing only stopwords.

	Parameters:
	- file_path (str): Path to the CSV file containing the text data. The CSV should have a single text column named "Text".
	- save_path (str, optional): Path where the histogram plot will be saved. If not provided, the plot is displayed.

	Returns:
	- matplotlib Axes object: If save_path is not provided and valid words are found in the input, the function
	displays the histogram plot and returns the matplotlib Axes object.
	- None: In two scenarios:
	1. If save_path is provided, saves the plot to the specified location and returns None.
	2. If the input file is empty or contains only stop words, prints a message and returns None.

	Requirements:
	- pandas
	- scikit-learn
	- matplotlib

	Examples:
	>>> ax = task_func('text_data.csv')
	# ax is the matplotlib Axes object for the plot
	>>> result = task_func('text_data.csv', 'output_plot.png')
	# result is None, and the plot is saved to 'output_plot.png'
	"""
	df = pd.read_csv(file_path, header=None, names=["Text"])
	df["Text"] = df["Text"].str.split("\\n").str.join(" ")

	vectorizer = CountVectorizer(stop_words=STOP_WORDS)
	try:
		word_count = vectorizer.fit_transform(df["Text"])
	except ValueError:
		# Handle the case where the DataFrame is empty or contains only stop words
		print("No valid words to plot. Returning None.")
		return None

	sum_words = word_count.sum(axis=0)
	words_freq = [
		(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()
	]
	words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

	top_words = words_freq[:10]
	df = pd.DataFrame(top_words, columns=["Word", "Count"])

	ax = df.plot.bar(x="Word", y="Count", rot=0)

	if not save_path:
		return ax
	plt.savefig(save_path)
	plt.close()
	return None
