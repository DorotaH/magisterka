def position_min(list1):
    min_val = min(list1)
    min_result = []
    for i, j in enumerate(list1):
        if j == min_val:
            min_result.append(i)
    return min_result
