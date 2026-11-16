def max_product(arr, n):
    mpis = [0] * (n)
    for i in range(0, n):
        mpis[i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and mpis[i] < (mpis[j] * arr[i]):
                mpis[i] = arr[i] * mpis[j]
    return max(mpis)
