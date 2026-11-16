def max_len_sub(arr, n):
    max = 0
    mls = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) <= 1 and mls[i] < 1 + mls[j]:
                mls[i] = 1 + mls[j]
    for i in range(n):
        max = max(max, mls[i])
    return max
