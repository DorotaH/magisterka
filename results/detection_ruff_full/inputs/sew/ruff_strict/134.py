def check_last(arr, n, p):
    _sum = 0
    for i in range(n):
        _sum += arr[i]
    if p == 1:
        if _sum % 2 == 0:
            return "ODD"
        return "EVEN"
    return "EVEN"
