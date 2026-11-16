def sum_three_smallest_nums(lst):
    return sum(sorted([x for x in lst if 0 < x])[:3])
