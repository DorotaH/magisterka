def first_Missing_Positive(arr, n):
    ptr = 0
    for i in range(0, n):
        if 1 == arr[i]:
            ptr = 1
            break
    if 0 == ptr:
        return 1
    for i in range(0, n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    for i in range(0, n):
        arr[(arr[i] - 1) % n] += n
    for i in range(0, n):
        if n >= arr[i]:
            return 1 + i
    return 1 + n
