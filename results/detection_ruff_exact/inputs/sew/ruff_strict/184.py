def greater_specificnum(list, num):
    greater_specificnum = all(num <= x for x in list)
    return greater_specificnum
