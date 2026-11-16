def count_Occurrence(tup, lst):
    return sum(bool(item in lst)
           for item in tup)
