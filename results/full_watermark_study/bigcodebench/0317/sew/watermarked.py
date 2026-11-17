import  numpy as  np
from  sklearn.feature_extraction.text import  TfidfVectorizer
import  re


def task_func(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values
    which are returned as a dictionary.

    Parameters:
    example_str (str): The input string.

    Returns:
    dict: A dictionary with words as keys and TF-IDF scores as values.

    Requirements:
    - sklearn.feature_extraction.text.TfidfVectorizer
    - numpy
    - re

    Example:
    >>> tfidf_scores = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> print(tfidf_scores)
    {'dog': 0.3779644730092272, 'josie': 0.3779644730092272, 'mugsy': 0.3779644730092272, 'smith': 0.7559289460184544}
    """
    pattern = r'\[.*?\]'
    text = re.sub(pattern, '', example_str)
    if  not  text.strip():
        return  dict()

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix, feature_names = tfidf_vectorizer.fit_transform([text]), tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = dict(zip(feature_names, np.squeeze(tfidf_matrix.toarray())))

    return  tfidf_scores
