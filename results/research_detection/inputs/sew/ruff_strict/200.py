def position_max(list1):
    max_val = max(list1)
    max_result = []
    for i, j in enumerate(list1):
        if j == max_val:
            max_result.append(i)
    return max_result
