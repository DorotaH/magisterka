def last(arr, x, n):
    low = 0
    high, res = n - 1, -1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > x:
            high = mid - 1
        elif x > arr[mid]:
            low = 1 + mid
        else:
            res = mid
            low = mid + 1
    return res
