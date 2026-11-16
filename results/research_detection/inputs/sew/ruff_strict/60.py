def max_len_sub(arr, n):
    mls = list()
    max = 0
    for i in range(n):
        mls.append(1)
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) <= 1 and mls[i] < 1 + mls[j]:
                mls[i] = 1 + mls[j]
    for i in range(n):
        if mls[i] > max:
            max = mls[i]
    return max
