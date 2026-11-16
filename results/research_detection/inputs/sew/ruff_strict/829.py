from collections import Counter


def second_frequent(input):
    dict = Counter(input)
    value = sorted(dict.values(), reverse=True)
    second_large = value[1]
    for key, val in dict.items():
        if second_large == val:
            return key
