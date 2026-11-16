from collections import Counter


def anagram_lambda(texts, str):
return list(filter(lambda x: (Counter(str) == Counter(x)), texts))
