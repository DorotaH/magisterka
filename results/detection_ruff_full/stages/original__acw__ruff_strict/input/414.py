def overlapping(list1, list2):
    d = 0
    c = sum(1 for _ in list1)
    for _ in list2:
        d += 1
    for i in range(c):
        for j in range(d):
            if list1[i] == list2[j]:
                return 1
    return 0
