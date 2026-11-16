from itertools import groupby 


def extract_elements(numbers, n):
    return [i for i, j in groupby(numbers) if len(list(j)) == n]
