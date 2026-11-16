def Odd_Length_Sum(arr):
    l = len(arr)
    return sum(((((i + 1) *(l - i) + 1) // 2) * arr[i]) for i in range(l))