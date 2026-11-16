from collections import Counter
def count_common(words):
  word_counts = Counter(words)
  return word_counts.most_common(4)
