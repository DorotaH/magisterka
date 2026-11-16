def min_Num(arr, n):
    odd = sum(bool(arr[i] % 2) for i in range(n))
    return 1 if (odd % 2) else 2
