def count_Char(str, x):
    count = sum(bool(str[i] == x) for i in range(len(str)))
    n = 10
    repititions = n // len(str)
    count = repititions * count
    l = n % len(str)
    for i in range(l):
        if str[i] == x:
            count += 1
    return count
