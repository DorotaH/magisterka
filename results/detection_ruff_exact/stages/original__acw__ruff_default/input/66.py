def pos_count(list):
    return sum(bool(num >= 0)
           for num in list)
