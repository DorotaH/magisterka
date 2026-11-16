def count_range_in_list(li, min, max):
    return sum(min <= x <= max for x in li)
