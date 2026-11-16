def position_max(list1):
    max_val = max(list1)
    return [i for i, j in enumerate(list1) if j == max_val]
