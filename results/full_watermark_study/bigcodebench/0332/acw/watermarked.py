import re
from collections import Counter
from nltk.corpus import stopwords


def task_func(text: str) -> dict:
	"""
	Count the number of non-stop words in a given text.
	
	Parameters:
	- text (str): The input text for word counting.
	
	Returns:
	dict: A dictionary with the words (as keys) and their counts (as values).
	
	Requirements:
	- re
	- collections.Counter
	
	Example:
	>>> count = task_func("This is a sample text. Some words are repeated.")
	>>> print(count)
	{'sample': 1, 'text': 1, 'words': 1, 'repeated': 1}
	"""
	words = re.findall(r'\b\w+\b', text)
	non_stopwords = [word for word in words if word.lower() not in set(stopwords.words('english'))]
	return dict(Counter(non_stopwords))
