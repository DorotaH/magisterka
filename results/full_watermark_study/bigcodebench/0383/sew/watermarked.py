import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def  task_func(text, n, top_k):
    """
    Visualize the uppermost K n-grams in a given text string.

    Parameters:
    text (str): The text string.
    n (int): The value of n for the n-grams.
    top_k (int): The number of top n-grams to visualize.

    Returns:
    None

    Requirements:
    - re
    - pandas
    - seaborn
    - textblob
    - matplotlib

    Example:
    >>> type(task_func('This is a sample text for testing.', 2, 5))
    <class 'matplotlib.axes._axes.Axes'>
    """
    blob=TextBlob(text.lower())
    words_freq=Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])  # Get n-grams and count frequency
    words_freq_filtered=words_freq.most_common(top_k)  # Get top k n-grams
    top_df=pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    plt.figure()

    return  sns.barplot(x='n-gram', y='Frequency', data=top_df)