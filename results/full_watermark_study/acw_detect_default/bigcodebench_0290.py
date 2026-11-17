import nltk

nltk.download("stopwords")
import os
from collections import Counter

from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words("english"))


def task_func(directory_path):
	"""
	Count the number of unique non-stop words across all '.txt' files in a specified directory.

	Parameters:
	directory_path (str): The path to the directory containing '.txt' files.

	Returns:
	int: The total count of unique non-stop words across all files.

	Requirements:
	- collections.Counter
	- os
	- nltk.corpus.stopwords

	Example:
	>>> task_func('./yourdictfiles/')
	1500
	"""

	word_counts = Counter()

	for file_name in os.listdir(directory_path):
		if not file_name.endswith(".txt"):
			continue
		with open(os.path.join(directory_path, file_name), "r") as file:
			words = [
				word for word in file.read().split() if word.lower() not in STOPWORDS
			]
			word_counts.update(words)

	return len(word_counts)
