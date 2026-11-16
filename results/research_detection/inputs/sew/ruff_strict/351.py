def first_Element(arr, n, k):
    count_map = dict()
    for i in range(n):
        if arr[i] not in count_map:
            count_map[arr[i]] = 1
        else:
            count_map[arr[i]] += 1
        i = i + 1
    for i in range(n):
        if k == count_map[arr[i]]:
            return arr[i]
        i = i + 1
    return -1
