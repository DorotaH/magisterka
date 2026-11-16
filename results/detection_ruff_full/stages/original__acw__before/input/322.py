def position_min(list1):
    min_val = min(list1)
    return [i for i, j in enumerate(list1) if j == min_val]