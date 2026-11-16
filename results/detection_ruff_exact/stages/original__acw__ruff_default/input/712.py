import itertools


def remove_duplicate(list1):
    list.sort(list1)
    return list(list1 for list1, _ in itertools.groupby(list1))
