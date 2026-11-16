import re
from collections import Counter


def n_common_words(text,n):
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)