import re
from collections import Counter

from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def task_func(input_string):
    """
    Divide a multi-line string into individual lines, remove stopwords, and count the frequency of each word.

    Parameters:
    - input_string (str): The multi-line string.

    Returns:
    - dict: A dictionary with word frequencies where each key is a unique word and the value is its frequency.

    Requirements:
    - re
    - nltk.corpus
    - collections

    Example:
    >>> task_func('line a\\nfollows by line b\\n...bye\\n')
    {'line': 2, 'follows': 1, 'b': 1, 'bye': 1}
    """
    lines = input_string.split("\n")
    word_count = Counter()
    for line in lines:
        words = re.findall(r"\b\w+\b", line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)
